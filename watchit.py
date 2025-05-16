#!/usr/bin/env python3
"""
WatchIt - A simple wrapper for TheWatcher Terminal Monitor
Just run: python watchit.py your_command
"""

import sys
import os
import subprocess

def main():
    """Run terminal_monitor.py with the given command."""
    if len(sys.argv) < 2:
        print("Usage: python watchit.py <command>")
        print("Example: python watchit.py python test_error.py")
        return
    
    # Get the command to monitor
    command = ' '.join(sys.argv[1:])
    
    # Construct the terminal_monitor.py command
    terminal_monitor_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "terminal_monitor.py")
    full_command = f"python {terminal_monitor_path} {command}"
    
    # Execute the command
    try:
        result = subprocess.run(full_command, shell=True)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nWatchIt terminated by user.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 