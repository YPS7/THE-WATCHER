# TheWatcher - AI-Powered Terminal Monitor

TheWatcher is a smart tool that watches your code as it runs and helps you fix errors automatically. It uses AI to understand what's going wrong and suggests solutions.

## What You Need

Before you start, make sure you have:
1. Windows 10 or later
2. Python 3.7 or later installed
3. An API key from one of these services:
   - OpenAI (GPT-3.5/4)
   - Google Gemini
   - Groq

## Step-by-Step Installation

### Step 1: Download the Files
1. Download these three files and put them in a folder:
   - `terminal_monitor.py`
   - `requirements.txt`
   - `install.bat`

### Step 2: Install Python Packages
1. Open PowerShell or Command Prompt
2. Go to the folder where you saved the files
3. Run this command:
```powershell
pip install -r requirements.txt
```
4. Wait for the installation to complete

### Step 3: Install TheWatcher
1. Right-click on `install.bat`
2. Select "Run as administrator"
3. Wait for the installation to complete
4. You'll see a message saying "TheWatcher has been installed successfully!"
5. Close your PowerShell/Command Prompt window
6. Open a new PowerShell/Command Prompt window

## Using TheWatcher

### First Time Setup
The first time you run TheWatcher, it will:
1. Ask if you want to use saved settings (if you've used it before)
2. If you choose not to use saved settings:
   - Show you a list of AI providers to choose from
   - Ask for your API key (you can paste it)
3. Save your settings for future use

### Running Your Code
You can run any type of code file:

1. **Python Files**:
```powershell
thewatcher "python your_script.py"
```

2. **JavaScript Files**:
```powershell
thewatcher "node your_script.js"
```

3. **Java Files**:
```powershell
thewatcher "javac YourFile.java"
thewatcher "java YourFile"
```

4. **Any Other Command**:
```powershell
thewatcher "your command here"
```

### How It Works
1. TheWatcher runs your code
2. If it finds any errors, it will:
   - Show you what went wrong
   - Ask if you want help fixing it
   - Use AI to analyze the error
   - Suggest a solution

## Troubleshooting

### If TheWatcher Command Doesn't Work
1. Make sure you ran `install.bat` as administrator
2. Try restarting your computer
3. Try running it with the full path:
```powershell
%LOCALAPPDATA%\TheWatcher\thewatcher.bat "your command"
```

### If You Get "Module Not Found" Error
1. Make sure you installed the requirements:
```powershell
pip install -r requirements.txt
```

### If You Get "File Not Found" Error
1. Make sure you're in the right folder
2. Check if the file you're trying to run exists

### If API Key Doesn't Work
1. Make sure you're using the correct API key
2. Try entering the API key again:
   - Delete the `.thewatcher` folder in your home directory
   - Run TheWatcher again to set up a new API key

## Getting API Keys

### OpenAI API Key
1. Go to https://platform.openai.com
2. Sign up or log in
3. Go to "API Keys"
4. Create a new API key

### Google Gemini API Key
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key

### Groq API Key
1. Go to https://console.groq.com
2. Sign up or log in
3. Get your API key from the dashboard

## Need Help?
If you run into any problems:
1. Check the error message carefully
2. Make sure you followed all installation steps
3. Try running the installation again
4. If the problem persists, create an issue on GitHub

## License
MIT License 