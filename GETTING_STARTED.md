# Getting Started with TheWatcher

This guide will help you set up and use TheWatcher on your system. Follow these steps carefully, and you'll be up and running in no time!

## Step 1: Download Required Files

First, you need to download these 4 files:
1. `terminal_monitor.py` - The main program
2. `requirements.txt` - List of required Python packages
3. `setup.py` - Installation script
4. `README.md` - Basic documentation

Save all these files in a folder on your computer. For example:
```
C:\Users\YourName\TheWatcher\
```

## Step 2: Install Python

If you don't have Python installed:
1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Download the latest Python version (3.7 or higher)
4. Run the installer
5. **Important**: Check the box that says "Add Python to PATH" during installation

To verify Python is installed:
1. Open your terminal/command prompt
2. Type: `python --version`
3. You should see something like `Python 3.9.0`

## Step 3: Install TheWatcher

1. Open your terminal/command prompt
2. Navigate to the folder where you saved the files:
```bash
cd C:\Users\YourName\TheWatcher
```

3. Install TheWatcher:
```bash
pip install -e .
```

You should see some text showing the installation progress. Wait until it completes.

## Step 4: Get an API Key

You'll need an API key from one of these services:
- OpenAI (recommended for beginners)
- Google Gemini
- Groq

### Getting an OpenAI API Key (Easiest Option):
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Click on your profile picture → "View API keys"
4. Click "Create new secret key"
5. Copy your new API key (keep it safe!)

## Step 5: Run Your First Command

Now you're ready to use TheWatcher! Here are some examples:

### Example 1: Running a Python File
```bash
thewatcher "python test.py"
```

### Example 2: Running a JavaScript File
```bash
thewatcher "node app.js"
```

### Example 3: Running an npm Command
```bash
thewatcher "npm start"
```

## What to Expect

When you run your first command:
1. You'll see a welcome message
2. You'll be asked to choose an AI provider (select 1 for OpenAI)
3. You'll be asked for your API key (paste it and press Enter)
4. TheWatcher will start monitoring your command

## Common Examples

### Python Examples:
```bash
# Run a Python script
thewatcher "python my_script.py"

# Run a Python script with arguments
thewatcher "python my_script.py --input data.txt"

# Run a specific Python file
thewatcher "python C:\path\to\your\script.py"
```

### JavaScript Examples:
```bash
# Run a Node.js script
thewatcher "node app.js"

# Run an npm command
thewatcher "npm run dev"

# Run a specific JavaScript file
thewatcher "node C:\path\to\your\script.js"
```

### Other Examples:
```bash
# Run a shell script
thewatcher "bash script.sh"

# Run a command with arguments
thewatcher "python script.py --debug --verbose"

# Run a command in a specific directory
thewatcher "cd C:\my\project && npm start"
```

## Troubleshooting

### If you get "command not found":
1. Make sure you installed TheWatcher correctly
2. Try running: `python terminal_monitor.py "your command"`

### If you get API key errors:
1. Make sure you entered the correct API key
2. Try setting it as an environment variable:
```bash
# For Windows
set OPENAI_API_KEY=your-key-here

# For Mac/Linux
export OPENAI_API_KEY=your-key-here
```

### If you get Python errors:
1. Make sure Python is installed correctly
2. Try running: `python --version`
3. Make sure you're using Python 3.7 or higher

## Need Help?

If you encounter any issues:
1. Check the error message carefully
2. Make sure all files are in the correct location
3. Verify your API key is correct
4. Try running the command without TheWatcher first to make sure it works

## Next Steps

Once you're comfortable with basic usage, you can:
1. Try different AI providers
2. Use environment variables for API keys
3. Create a configuration file
4. Explore more advanced features

Remember: TheWatcher is here to help you debug your code. If you see an error, it will analyze it and suggest fixes automatically! 