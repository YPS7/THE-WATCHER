# TheWatcher PowerShell Wrapper
# A simple PowerShell script to run TheWatcher with easier syntax

param (
    [Parameter(Position=0, Mandatory=$true)]
    [ValidateSet("run", "fix", "help", "version")]
    [string]$Command,
    
    [Parameter(Position=1, ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

# Get the script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$cliPath = Join-Path -Path $scriptPath -ChildPath "thewatcher_cli.py"

# Check if the cli script exists
if (-not (Test-Path $cliPath)) {
    Write-Host "Error: thewatcher_cli.py not found. Please run install.py first." -ForegroundColor Red
    exit 1
}

# Run the appropriate command
switch ($Command) {
    "run" {
        if ($Arguments.Count -eq 0) {
            Write-Host "Error: No command specified to run." -ForegroundColor Red
            Write-Host "Usage: .\thewatcher.ps1 run <command>" -ForegroundColor Yellow
            exit 1
        }
        
        $cmdToRun = $Arguments -join " "
        $monitorPath = Join-Path -Path $scriptPath -ChildPath "terminal_monitor.py"
        
        try {
            & python $monitorPath $cmdToRun
        }
        catch {
            Write-Host "Error running command: $_" -ForegroundColor Red
            exit 1
        }
    }
    
    "fix" {
        if ($Arguments.Count -eq 0) {
            Write-Host "Error: No file specified to fix." -ForegroundColor Red
            Write-Host "Usage: .\thewatcher.ps1 fix <file>" -ForegroundColor Yellow
            exit 1
        }
        
        # For now, just show a message since fix isn't fully implemented
        Write-Host "Coming soon: Fix-error functionality!" -ForegroundColor Cyan
    }
    
    "version" {
        Write-Host "TheWatcher v1.0.0" -ForegroundColor Cyan
    }
    
    "help" {
        Write-Host "TheWatcher - Error monitoring and fixing tool" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Commands:" -ForegroundColor Yellow
        Write-Host "  run <command>    - Run a command with error monitoring" -ForegroundColor White
        Write-Host "  fix <file>       - Analyze errors in a file" -ForegroundColor White
        Write-Host "  version          - Show version information" -ForegroundColor White
        Write-Host "  help             - Show this help message" -ForegroundColor White
        Write-Host ""
        Write-Host "Examples:" -ForegroundColor Yellow
        Write-Host "  .\thewatcher.ps1 run python test_error.py" -ForegroundColor White
        Write-Host "  .\thewatcher.ps1 run node test_error.js" -ForegroundColor White
    }
} 