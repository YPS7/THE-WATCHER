# TheWatcher - AI-Powered Terminal Error Monitor

TheWatcher is an intelligent terminal monitor that watches for errors in your command outputs and provides AI-powered solutions to fix them.

## Features

- Real-time error detection in terminal commands
- AI-powered error analysis and solutions
- Support for multiple AI providers (OpenAI, Google Gemini, Groq)
- Beautiful terminal interface with Rich
- Automatic error pattern recognition

## Quick Installation

1. Download these files:
   - `terminal_monitor.py`
   - `requirements.txt`
   - `setup.py`
   - `README.md`

2. Open your terminal in the directory containing these files and run:
```bash
pip install -e .
```

## Usage

Run TheWatcher with any command you want to monitor:

```bash
# For Python files
thewatcher "python your_script.py"

# For JavaScript files
thewatcher "node your_script.js"

# For npm commands
thewatcher "npm start"

# For any other command
thewatcher "your command here"
```

When you first run TheWatcher, it will:
1. Display a welcome message
2. Ask you to select your preferred AI provider (OpenAI, Google Gemini, or Groq)
3. Prompt for your API key
4. Start monitoring your command

## Setting up API Keys

You can provide your API key in several ways:

1. When prompted (first run)
2. Environment variable:
```bash
# For OpenAI
set OPENAI_API_KEY=your-key-here

# For Google Gemini
set GOOGLE_API_KEY=your-key-here

# For Groq
set GROQ_API_KEY=your-key-here
```

3. Command line:
```bash
thewatcher --provider "OpenAI" --api-key "your-key-here" "your command"
```

## Supported AI Providers

- OpenAI (GPT-3.5/4)
- Google Gemini
- Groq

## Requirements

- Python 3.7+
- An API key from one of the supported AI providers

## Troubleshooting

If you get a "command not found" error:
1. Make sure you've installed the package using `pip install -e .`
2. Try running with the full path: `python terminal_monitor.py "your command"`

## License

MIT License 