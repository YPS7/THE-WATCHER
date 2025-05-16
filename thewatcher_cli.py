#!/usr/bin/env python3
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
            print("\nTheWatcher terminated by user.")
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
        print("\nExamples:")
        print("  thewatcher run python test_error.py       - Run a Python script with error monitoring")
        print("  thewatcher run node test_error.js         - Run a JavaScript program with error monitoring")
        sys.exit(0)

if __name__ == "__main__":
    main()
