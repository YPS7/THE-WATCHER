#!/usr/bin/env python3
"""
Installer for TheWatcher

This script installs TheWatcher as a command-line tool that can be activated from any directory.
"""

import os
import sys
import site
import shutil
import subprocess
from pathlib import Path

# ANSI color codes for prettier output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_color(message, color=GREEN, bold=False):
    """Print colored text to the console."""
    prefix = BOLD if bold else ""
    print(f"{prefix}{color}{message}{RESET}")

def is_windows():
    """Check if running on Windows."""
    return sys.platform.startswith("win")

def get_scripts_dir():
    """Get the scripts directory based on platform."""
    if is_windows():
        return os.path.join(sys.prefix, "Scripts")
    else:
        return os.path.join(sys.prefix, "bin")

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = ["rich", "openai"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print_color(f"Missing required packages: {', '.join(missing_packages)}", RED, bold=True)
        install = input(f"{YELLOW}Do you want to install them now? (y/n): {RESET}")
        if install.lower() == 'y':
            print_color("Installing missing packages...", BLUE)
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print_color("Dependencies installed successfully!", GREEN)
        else:
            print_color("Please install the required packages and run the installer again.", RED)
            sys.exit(1)
    else:
        print_color("All dependencies are installed.", GREEN)

def install_thewatcher():
    """Install TheWatcher CLI tool."""
    # Get current directory (where the script is running)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Try global installation first
        print_color("Attempting global installation...", BLUE)
        install_global()
        print_color("Global installation successful!", GREEN, bold=True)
    except (PermissionError, OSError) as e:
        print_color(f"Global installation failed due to permissions: {e}", YELLOW)
        print_color("Falling back to local installation...", BLUE)
        
        # Create local batch/shell files in the current directory
        if is_windows():
            # Create a batch file
            batch_file = os.path.join(current_dir, "thewatcher.bat")
            with open(batch_file, "w") as f:
                f.write(f"""@echo off
REM TheWatcher local installation
python "{os.path.join(current_dir, 'thewatcher_cli.py')}" %*
""")
            print_color(f"Created local batch file: {batch_file}", GREEN)
            print_color("To use TheWatcher, run it from this directory or add this directory to your PATH.", YELLOW)
        else:
            # Create a shell script
            shell_file = os.path.join(current_dir, "thewatcher")
            with open(shell_file, "w") as f:
                f.write(f"""#!/usr/bin/env python3
import sys
import os
import subprocess

# Path to the thewatcher_cli.py
THEWATCHER_PATH = "{os.path.join(current_dir, 'thewatcher_cli.py')}"

if __name__ == "__main__":
    # Pass all arguments to the thewatcher_cli.py script
    cmd = [sys.executable, THEWATCHER_PATH] + sys.argv[1:]
    subprocess.run(cmd)
""")
            # Make the file executable
            os.chmod(shell_file, 0o755)
            print_color(f"Created local shell script: {shell_file}", GREEN)
            print_color("To use TheWatcher, run it from this directory, create a symlink, or add this directory to your PATH.", YELLOW)
    
    # Create the .env.thewatcher file if it doesn't exist
    env_file = os.path.join(current_dir, '.env.thewatcher')
    if not os.path.exists(env_file):
        print_color("Creating default .env.thewatcher file...", BLUE)
        with open(env_file, 'w') as f:
            f.write("""# TheWatcher environment configuration
# Replace with your actual API keys
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
THEWATCHER_PREFERRED_PROVIDER=openai
THEWATCHER_CACHE_ENABLED=true
""")
        print_color("Default .env.thewatcher file created. Please edit it with your API keys.", YELLOW)

def install_global():
    """Install TheWatcher globally (may require elevated permissions)."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = get_scripts_dir()
    
    # Ensure scripts directory exists
    os.makedirs(scripts_dir, exist_ok=True)
    
    # Create command file with appropriate extension
    command_file = os.path.join(scripts_dir, "thewatcher.exe" if is_windows() else "thewatcher")
    
    # Windows requires a special batch file
    if is_windows():
        with open(os.path.join(scripts_dir, "thewatcher.bat"), "w") as f:
            f.write(f"""@echo off
@python "{os.path.join(current_dir, 'thewatcher_cli.py')}" %*
""")
    
    # Create a Unix executable script
    else:
        with open(command_file, "w") as f:
            f.write(f"""#!/usr/bin/env python3
import sys
import os
import subprocess

# Path to the thewatcher_cli.py
THEWATCHER_PATH = "{os.path.join(current_dir, 'thewatcher_cli.py')}"

if __name__ == "__main__":
    # Pass all arguments to the thewatcher_cli.py script
    cmd = [sys.executable, THEWATCHER_PATH] + sys.argv[1:]
    subprocess.run(cmd)
""")
        # Make the file executable
        os.chmod(command_file, 0o755)
    
    print_color(f"TheWatcher command installed at: {command_file if not is_windows() else os.path.join(scripts_dir, 'thewatcher.bat')}", GREEN)

def main():
    """Run the installer."""
    print_color("=== TheWatcher Installer ===", BLUE, bold=True)
    
    # Check dependencies
    check_dependencies()
    
    # Create the CLI script if it doesn't exist
    cli_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thewatcher_cli.py")
    if not os.path.exists(cli_script_path):
        print_color("Creating TheWatcher CLI script...", BLUE)
        create_cli_script()
    
    # Install the command
    install_thewatcher()
    
    print_color("\nInstallation complete!", GREEN, bold=True)
    print_color("You can now use TheWatcher with the following commands:", BLUE)
    print_color("  thewatcher run <command>    - Run a command with error monitoring", RESET)
    print_color("  thewatcher fix <file>       - Analyze errors in a file", RESET)
    print_color("  thewatcher help             - Show help information", RESET)
    
    print_color("\nImportant:", YELLOW, bold=True)
    print_color("Make sure to edit the .env.thewatcher file with your API keys.", YELLOW)

def create_cli_script():
    """Create the thewatcher_cli.py script."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cli_script_path = os.path.join(current_dir, "thewatcher_cli.py")
    
    with open(cli_script_path, "w") as f:
        f.write('''#!/usr/bin/env python3
"""
TheWatcher CLI - Command line interface for TheWatcher
"""

import sys
import os
import subprocess
import argparse

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="TheWatcher CLI - Monitor and fix errors in your commands")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a command with error monitoring")
    run_parser.add_argument("cmd", nargs="+", help="The command to run")
    
    # Fix command
    fix_parser = subparsers.add_parser("fix", help="Fix errors in a file")
    fix_parser.add_argument("file", help="The file containing errors")
    fix_parser.add_argument("--provider", help="The AI provider to use (openai, groq, gemini)")
    
    # Version command
    subparsers.add_parser("version", help="Show version information")
    
    # Help command
    subparsers.add_parser("help", help="Show help information")
    
    args = parser.parse_args()
    
    # Current directory where thewatcher_cli.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    if args.command == "run":
        # Run the command with terminal_monitor.py
        cmd = " ".join(args.cmd)
        monitor_script = os.path.join(current_dir, "terminal_monitor.py")
        monitor_cmd = f"python {monitor_script} {cmd}"
        
        try:
            result = subprocess.run(monitor_cmd, shell=True)
            sys.exit(result.returncode)
        except KeyboardInterrupt:
            print("\\nTheWatcher terminated by user.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    elif args.command == "fix":
        # TODO: Implement fix-error functionality
        print("Coming soon: Fix-error functionality!")
        sys.exit(0)
    
    elif args.command == "version":
        print("TheWatcher v1.0.0")
        sys.exit(0)
    
    elif args.command == "help" or args.command is None:
        parser.print_help()
        print("\\nExamples:")
        print("  thewatcher run python test_error.py       - Run a Python script with error monitoring")
        print("  thewatcher run node test_error.js         - Run a JavaScript program with error monitoring")
        sys.exit(0)

if __name__ == "__main__":
    main()
''')
    
    # Make the file executable
    os.chmod(cli_script_path, 0o755)

if __name__ == "__main__":
    main() 