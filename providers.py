"""Provider implementation for TheWatcher."""
import os
from typing import Dict, Any, Optional
import openai

class OpenAIProvider:
    """Provider implementation for OpenAI."""
    
    def __init__(self, api_key: str):
        """Initialize the OpenAI provider."""
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)
    
    async def analyze(self, error_context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze an error using OpenAI."""
        error_message = error_context.get("message", "Unknown error")
        raw_error = error_context.get("raw", "")
        
        prompt = f"""
        You are a programming assistant. Help debug the following error:
        
        Error message: {error_message}
        
        Full error:
        {raw_error}
        
        Please provide:
        1. A brief explanation of what caused the error
        2. A solution to fix the error
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI programming assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            explanation = response.choices[0].message.content
            
            return {
                "error": error_message,
                "explanation": explanation,
                "solution": "See explanation above for the solution.",
                "confidence": 0.9
            }
        except Exception as e:
            return {
                "error": error_message,
                "explanation": f"Error analyzing with OpenAI: {str(e)}",
                "solution": "Could not generate a solution due to API error.",
                "confidence": 0.0
            }

def get_provider(provider_name: str, config: Dict[str, Any]):
    """Get a provider implementation."""
    if provider_name == "openai":
        api_key = config.get("api", {}).get("openai") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No OpenAI API key found")
        return OpenAIProvider(api_key)
    else:
        # Default to OpenAI
        api_key = config.get("api", {}).get("openai") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No OpenAI API key found")
        return OpenAIProvider(api_key) 