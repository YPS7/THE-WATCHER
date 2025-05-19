#!/usr/bin/env python3
"""
Terminal Monitor for TheWatcher.
This script monitors command outputs for errors and offers fixes automatically.
"""

import os
import sys
import re
import subprocess
import tempfile
import asyncio
import random
import hashlib
import argparse
import json
from datetime import datetime
from typing import Dict, Any
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.markdown import Markdown

try:
    from dotenv import load_dotenv
    # Try to load environment variables
    try:
        load_dotenv(".env.thewatcher")
    except Exception:
        pass
except ImportError:
    # dotenv not installed, continue without it
    pass

# Setup Rich console
console = Console()

# Witty welcome messages
WELCOME_MESSAGES = [
    "TheWatcher activated! I'm keeping an eye on those pesky errors for you.",
    "Error hunter extraordinaire at your service! Let's squash some bugs today.",
    "TheWatcher is online. Your code's new best friend has arrived!",
    "Bug detection mode: ACTIVATED. I'll be your coding sidekick today!",
    "TheWatcher is on duty. No error shall pass unnoticed!",
]

# Import needed AI libraries
try:
    import openai
    import google.generativeai as genai
    import groq
except ImportError:
    console.print("[bold red]Required AI libraries not installed. Please install them with: pip install -r requirements.txt[/]")
    sys.exit(1)

class TerminalMonitor:
    """Monitors terminal commands and analyzes errors."""
    
    def __init__(self, provider=None, api_key=None):
        """Initialize the terminal monitor."""
        self.api_key = api_key
        self.provider = provider
        self.setup_ai_provider()
        
        # Welcome message
        welcome_msg = random.choice(WELCOME_MESSAGES)
        console.print(Panel(f"[bold green]{welcome_msg}[/]", title="TheWatcher"))
    
    def load_config(self):
        """Load configuration from config file."""
        config_paths = [
            os.path.join(os.path.expanduser("~"), ".thewatcher", "config.json"),
            ".thewatcher.json",
            "config.json"
        ]
        
        for path in config_paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        return json.load(f)
                except:
                    continue
        return {}
    
    def save_config(self, provider, api_key):
        """Save configuration to file."""
        config_dir = os.path.join(os.path.expanduser("~"), ".thewatcher")
        os.makedirs(config_dir, exist_ok=True)
        config_path = os.path.join(config_dir, "config.json")
        
        config = {
            "provider": provider,
            "api_key": api_key
        }
        
        with open(config_path, 'w') as f:
            json.dump(config, f)
    
    def setup_ai_provider(self):
        """Set up the AI provider and get API key."""
        providers = {
            "1": ("OpenAI", "OPENAI_API_KEY"),
            "2": ("Google Gemini", "GOOGLE_API_KEY"),
            "3": ("Groq", "GROQ_API_KEY")
        }
        
        # If provider and API key are already set, use them
        if self.provider and self.api_key:
            provider_name = self.provider
            env_var = next((v[1] for k, v in providers.items() if v[0] == provider_name), None)
            if env_var:
                os.environ[env_var] = self.api_key
                self.initialize_provider(provider_name, self.api_key)
                return
        
        # Try to load from config
        config = self.load_config()
        if config.get("provider") and config.get("api_key"):
            self.provider = config["provider"]
            self.api_key = config["api_key"]
            env_var = next((v[1] for k, v in providers.items() if v[0] == self.provider), None)
            if env_var:
                os.environ[env_var] = self.api_key
                self.initialize_provider(self.provider, self.api_key)
                return
        
        # Try to get from environment variables
        for key, (name, env_var) in providers.items():
            if os.getenv(env_var):
                self.provider = name
                self.api_key = os.getenv(env_var)
                self.initialize_provider(name, self.api_key)
                return
        
        # If still no provider set, ask user
        if not self.provider:
            # Display provider options
            console.print("\n[bold cyan]Select your AI provider:[/]")
            for key, (name, _) in providers.items():
                console.print(f"{key}. {name}")
            
            # Get provider choice
            while True:
                try:
                    choice = Prompt.ask("\nEnter your choice (1-3)", default="1")
                    if choice in providers:
                        self.provider = providers[choice][0]
                        env_var = providers[choice][1]
                        break
                    console.print("[red]Invalid choice. Please select 1-3.[/]")
                except:
                    # If prompt fails, use default
                    self.provider = "OpenAI"
                    env_var = "OPENAI_API_KEY"
                    break
        
        # If still no API key, ask user
        if not self.api_key:
            while True:
                try:
                    self.api_key = Prompt.ask(f"\nEnter your {self.provider} API key", password=True)
                    if self.api_key.strip():
                        break
                    console.print("[red]API key cannot be empty.[/]")
                except:
                    console.print("[red]Could not get API key interactively. Please set it via environment variable or config file.[/]")
                    sys.exit(1)
        
        # Save to config
        self.save_config(self.provider, self.api_key)
        
        # Set environment variable
        env_var = next((v[1] for k, v in providers.items() if v[0] == self.provider), None)
        if env_var:
            os.environ[env_var] = self.api_key
        
        # Initialize provider
        self.initialize_provider(self.provider, self.api_key)
    
    def initialize_provider(self, provider, api_key):
        """Initialize the selected AI provider."""
        if provider == "OpenAI":
            self.client = openai.OpenAI(api_key=api_key)
        elif provider == "Google Gemini":
            genai.configure(api_key=api_key)
            self.client = genai
        elif provider == "Groq":
            self.client = groq.Client(api_key=api_key)
    
    async def analyze_error(self, error_text):
        """Analyze an error and suggest fixes."""
        # Parse the error
        error_context = self.parse_error(error_text)
        
        # Ask user if they want a fix
        if not Confirm.ask("[yellow]Detected an error. Would you like me to analyze it and suggest a fix?[/]"):
            return
        
        console.print("[cyan]Analyzing error...[/]")
        
        try:
            # Prepare the error prompt
            error_message = error_context.get("message", "Unknown error")
            prompt = f"""
            You are a programming assistant. Help debug the following error:
            
            Error message: {error_message}
            
            Full error:
            {error_text}
            
            Please provide:
            1. A brief explanation of what caused the error
            2. A solution to fix the error
            """
            
            try:
                with console.status("[bold green]Consulting AI for solutions...[/]"):
                    if self.provider == "OpenAI":
                        response = self.client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful AI programming assistant."},
                                {"role": "user", "content": prompt}
                            ]
                        )
                        explanation = response.choices[0].message.content
                    elif self.provider == "Google Gemini":
                        model = self.client.GenerativeModel('gemini-pro')
                        response = model.generate_content(prompt)
                        explanation = response.text
                    elif self.provider == "Groq":
                        response = self.client.chat.completions.create(
                            model="mixtral-8x7b-32768",
                            messages=[
                                {"role": "system", "content": "You are a helpful AI programming assistant."},
                                {"role": "user", "content": prompt}
                            ]
                        )
                        explanation = response.choices[0].message.content
                
                # Format and display the response
                result = {
                    "error": error_message,
                    "explanation": explanation,
                    "solution": "See explanation above for the solution.",
                    "confidence": 0.9
                }
                
                self.format_response(result)
            except Exception as api_error:
                console.print(f"[yellow]Error with {self.provider} API: {api_error}[/]")
                console.print("[yellow]Providing local analysis instead...[/]")
                
                # Provide a basic analysis based on the error type
                if "TypeError: can only concatenate str (not \"int\") to str" in error_text:
                    result = {
                        "error": "TypeError: can only concatenate str (not \"int\") to str",
                        "explanation": "This error occurs when you try to add (concatenate) a string and an integer directly in Python. Python cannot automatically convert between these types.",
                        "solution": "Convert the integer to a string using the `str()` function before concatenation. For example: `text + str(num)` instead of `text + num`.",
                        "confidence": 0.95
                    }
                elif "ZeroDivisionError" in error_text:
                    result = {
                        "error": "ZeroDivisionError",
                        "explanation": "This error occurs when you attempt to divide by zero, which is mathematically undefined.",
                        "solution": "Add a check to ensure the denominator is not zero before performing division. Example: `if b != 0: result = a / b else: handle_zero_case()`",
                        "confidence": 0.95
                    }
                elif "IndexError" in error_text:
                    result = {
                        "error": "IndexError",
                        "explanation": "This error occurs when you try to access an index that is outside the bounds of a list or sequence.",
                        "solution": "Check that your index is within the valid range (0 to len(sequence)-1) before accessing it. Consider using a try/except block or a conditional check.",
                        "confidence": 0.95
                    }
                elif "KeyError" in error_text:
                    result = {
                        "error": "KeyError",
                        "explanation": "This error occurs when you try to access a dictionary key that doesn't exist.",
                        "solution": "Use dict.get(key) which returns None for missing keys, or check if the key exists with `if key in dict` before accessing it.",
                        "confidence": 0.95
                    }
                elif "NameError" in error_text:
                    result = {
                        "error": "NameError",
                        "explanation": "This error occurs when you try to use a variable or function that hasn't been defined.",
                        "solution": "Make sure the variable is defined before using it. Check for typos in variable names. Ensure the variable is defined in the current scope.",
                        "confidence": 0.95
                    }
                elif "TypeError" in error_text and "is not a function" in error_text:
                    result = {
                        "error": "TypeError: x is not a function",
                        "explanation": "This JavaScript error occurs when you try to call something that is not a function as if it were a function.",
                        "solution": "Check the type of the object before calling it. Make sure you're not using a property when you meant to use a method.",
                        "confidence": 0.95
                    }
                else:
                    result = {
                        "error": error_message,
                        "explanation": "This error typically occurs due to a mismatch between what the code is expecting and what it's actually receiving.",
                        "solution": "Check the values being used at the point of the error. Ensure types match what the operation requires. Consider adding more validation or error handling.",
                        "confidence": 0.6
                    }
                
                self.format_response(result)
                
        except Exception as e:
            console.print(Panel(f"[bold red]Error during analysis: {e}[/]"))
    
    def parse_error(self, error_text: str) -> Dict[str, Any]:
        """Simple error parser."""
        error_data = {
            "message": "",
            "raw": error_text
        }
        
        # Parse Python errors
        if "Traceback (most recent call last)" in error_text:
            error_match = re.search(r'([A-Za-z]+Error:.*?)(?:\n|$)', error_text, re.DOTALL)
            if error_match:
                error_data["message"] = error_match.group(1).strip()
        
        # Parse JavaScript errors
        elif any(marker in error_text for marker in ["Error:", "TypeError:", "SyntaxError:", "ReferenceError:"]):
            error_match = re.search(r'([A-Za-z]+Error:.*?)(?:\n|$)', error_text, re.DOTALL)
            if error_match:
                error_data["message"] = error_match.group(1).strip()
        
        # Generic fallback
        if not error_data["message"]:
            lines = error_text.strip().split('\n')
            if lines:
                error_data["message"] = lines[0].strip()
        
        return error_data
    
    def format_response(self, response: Dict[str, Any]) -> None:
        """Format and display a response."""
        error = response.get("error", "Unknown error")
        explanation = response.get("explanation", "No explanation available")
        solution = response.get("solution", "No solution available")
        confidence = response.get("confidence", 0.0)
        
        # Error panel
        console.print(Panel(f"[bold red]{error}[/]", title="Error"))
        
        # Explanation panel
        console.print(Panel(Markdown(explanation), title="Explanation"))
        
        # Solution panel if different from explanation
        if solution != "See explanation above for the solution.":
            console.print(Panel(Markdown(solution), title="Solution"))
        
        # Confidence
        confidence_color = "green" if confidence > 0.7 else "yellow" if confidence > 0.4 else "red"
        console.print(f"[{confidence_color}]Confidence: {confidence:.0%}[/]")
    
    def execute_command(self, command):
        """Execute a command and monitor for errors."""
        # Create temporary file to capture output
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            # Run the command and redirect output to file
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Stream output to console and check for errors
            output = []
            for line in process.stdout:
                sys.stdout.write(line)
                output.append(line)
            
            process.wait()
            full_output = ''.join(output)
            
            # Check for errors in output
            error_patterns = [
                r"Traceback \(most recent call last\)",  # Python
                r"[A-Za-z]+Error:",  # Generic errors
                r"Exception in thread",  # Java
                r"Caused by:",  # Java 
                r"npm ERR!",  # npm
                r"SyntaxError:",  # JavaScript
                r"ReferenceError:",  # JavaScript
                r"TypeError:"  # JavaScript
            ]
            
            if any(re.search(pattern, full_output) for pattern in error_patterns):
                # Found an error, run analysis
                asyncio.run(self.analyze_error(full_output))
            
            return process.returncode
            
        except Exception as e:
            console.print(f"[bold red]Error executing command: {e}[/]")
            return 1
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)

def main():
    """Run the terminal monitor."""
    parser = argparse.ArgumentParser(description="TheWatcher - AI-Powered Terminal Error Monitor")
    parser.add_argument("command", nargs="+", help="Command to monitor")
    parser.add_argument("--provider", choices=["OpenAI", "Google Gemini", "Groq"], help="AI provider to use")
    parser.add_argument("--api-key", help="API key for the selected provider")
    args = parser.parse_args()
    
    monitor = TerminalMonitor(provider=args.provider, api_key=args.api_key)
    
    # Get the command to monitor
    command = ' '.join(args.command)
    
    # Execute the command
    exit_code = monitor.execute_command(command)
    sys.exit(exit_code)

if __name__ == "__main__":
    main() 