# TheWatcher Terminal Monitor

The Terminal Monitor is a command wrapper that watches for errors in your terminal output and provides AI-powered fix suggestions.

## Setup

1. Make sure you have the TheWatcher project installed
2. Create a `.env.thewatcher` file in the project root with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   GEMINI_API_KEY=your_gemini_api_key
   THEWATCHER_PREFERRED_PROVIDER=openai
   THEWATCHER_CACHE_ENABLED=true
   ```

## Usage

Run any command through the terminal monitor:

```bash
python terminal_monitor.py "your command"
```

For example:

```bash
# Python example
python terminal_monitor.py "python test_error.py"

# JavaScript example
python terminal_monitor.py "node test_error.js"
```

## Features

- Auto-detects errors in command output
- Works with Python, JavaScript, Java, and other languages
- Prompts for your confirmation before analyzing errors
- Provides AI-generated fix suggestions
- No error logs stored on your system (completely ephemeral)
- Witty welcome messages!

## Test Files

The repository includes sample files that generate errors for testing:

- `test_error.py` - Python errors
- `test_error.js` - JavaScript errors

You can uncomment different error types in these files to test various error detection and fix scenarios.

## Requirements

- Python 3.8+
- Rich library
- python-dotenv
- TheWatcher installed 