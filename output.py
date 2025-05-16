"""Output formatting for TheWatcher."""
import json
from typing import Dict, Any
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def format_response(response: Dict[str, Any], output_format: str = "rich") -> None:
    """Format and display a response."""
    if output_format == "json":
        console.print(json.dumps(response, indent=2))
    elif output_format == "diff":
        console.print("Diff view not implemented in this simplified version")
    else:  # rich format
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