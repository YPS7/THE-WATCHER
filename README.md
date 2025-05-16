# TheWatcher

A CLI tool that checks console errors and provides possible fixes using AI-powered analysis.

## Features

- Intercepts and parses console errors from Python scripts, Node.js, browsers, or any CLI output
- Supports multiple AI providers (OpenAI, Groq, Gemini)
- Securely manages API keys
- Intelligent error analysis with contextual understanding
- Rich terminal output with colorized suggestions and code diffs
- Caching system to avoid redundant API calls
- Plugin architecture for extensibility
- **NEW**: Terminal Monitor for real-time error detection!
- **NEW**: Command-line installation for global access

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/thewatcher.git
cd thewatcher

# Run the installer script
python install.py
```

This will:
- Check for dependencies and install them if needed
- Install TheWatcher as a global command
- Set up a default configuration file

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/thewatcher.git
cd thewatcher

# Install with pip
pip install -e .
```

## Configuration

Set up your API keys in one of the following ways:

1. Environment variables:
   ```bash
   export OPENAI_API_KEY=your_openai_key
   export GROQ_API_KEY=your_groq_key
   export GEMINI_API_KEY=your_gemini_key
   ```

2. Create a config file at `~/.config/thewatcher/config.toml`:
   ```toml
   [api]
   openai = "your_openai_key"
   groq = "your_groq_key" 
   gemini = "your_gemini_key"
   
   [settings]
   preferred_provider = "openai"
   cache_enabled = true
   ```

3. Copy the example env file and modify it:
   ```bash
   cp .env.thewatcher.example .env.thewatcher
   # Edit .env.thewatcher with your API keys
   ```

## Usage

### Command-Line Interface

After running the installer, you can use TheWatcher from anywhere:

```bash
# Run a command with error monitoring
thewatcher run python script.py

# Get help information
thewatcher help

# Show version information
thewatcher version
```

### Terminal Monitor

The Terminal Monitor wraps your commands and automatically detects errors:

```bash
# Use the simple watchit.py script
python watchit.py python test_error.py

# Or use the terminal_monitor.py directly
python terminal_monitor.py "node test_error.js"

# Or use the new command-line tool (after installation)
thewatcher run python test_error.py
```

The Terminal Monitor:
- Displays a welcome message when activated
- Watches command output for errors in real-time
- Asks for confirmation before analyzing errors
- Provides AI-powered fix suggestions
- Handles Python, JavaScript, Java, and other languages
- Doesn't store error logs on your system

### Fixing errors from a file

```bash
thewatcher fix-error --file error.log
```

### Fixing errors from stdin (pipe from another command)

```bash
python script_with_errors.py 2>&1 | thewatcher fix-error
```

### Specify a particular provider

```bash
thewatcher fix-error --file error.log --provider openai
```

### Output formats

```bash
# JSON output
thewatcher fix-error --file error.log --output json

# Show raw diff
thewatcher fix-error --file error.log --output diff
```

## Test Files

The repository includes sample files that generate errors for testing:

- `test_error.py` - Python errors
- `test_error.js` - JavaScript errors

## License

MIT 