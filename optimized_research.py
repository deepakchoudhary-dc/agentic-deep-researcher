
import os
import requests
from typing import Type
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from linkup import LinkupClient

load_dotenv()

# Simple tool base class to replace CrewAI dependency
class SimpleTool:
    def __init__(self):
        self.name = ""
        self.description = ""
    
    def _run(self, query: str) -> str:
        raise NotImplementedError("Tool must implement _run method")

class OptimizedOllamaClient:
    """Optimized Ollama client for best speed/quality balance"""
    
    def __init__(self, model="qwen3:1.7b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url
    
    def generate(self, prompt: str) -> str:
        """Generate response with optimized settings"""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,                    "options": {
                        "temperature": 0.2,
                        "top_p": 0.8,
                        "top_k": 40,
                        "repeat_penalty": 1.1,
                        "num_ctx": 8192,        # Increased context window
                        "num_predict": 4096,    # Much higher token limit for full responses
                        "num_thread": -1,       # Use all CPU threads
                        "stop": []              # Remove all stop tokens to prevent early termination
                    }
                },
                timeout=180  # Increased timeout for longer responses
            )
            
            if response.status_code == 200:
                result = response.json()
                text = result.get('response', '')
                  # Minimal cleaning - only remove obvious thinking blocks, preserve all content
                import re
                # Only remove explicit thinking tags, keep everything else
                if '<think>' in text and '</think>' in text:
                    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
                
                # Don't remove any other content - let the model generate fully
                text = text.strip()
                
                return text if text else "Response generated but appears empty"
            else:
                return f"HTTP Error {response.status_code}"
                
        except Exception as e:
            return f"Generation error: {str(e)}"

class OptimizedSearchTool(SimpleTool):
    def __init__(self):
        super().__init__()
        self.name = "Optimized Search"
        self.description = "Fast web search with LinkUp"
    
    def _run(self, query: str) -> str:
        try:
            client = LinkupClient(api_key=os.getenv("LINKUP_API_KEY"))
            response = client.search(
                query=query,
                depth="standard",
                output_type="searchResults"
            )
            return str(response)[:8000]  # Increased limit for more comprehensive search results
        except Exception as e:
            return f"Search error: {str(e)}"

def optimized_research(query: str) -> str:
    """Optimized research for speed and detail"""
    try:
        print(f"🔍 Researching: {query}")
        
        if not os.getenv("LINKUP_API_KEY"):
            return "❌ Please set your LINKUP_API_KEY environment variable"
        
        llm = OptimizedOllamaClient()
        search_tool = OptimizedSearchTool()
        
        print("📡 Searching web...")
        search_results = search_tool._run(query)
        
        if "Search error:" in search_results:
            return f"❌ Search failed: {search_results}"
        
        print("🧠 Analyzing and generating response...")
          # Enhanced prompt for complete, detailed responses
        prompt = f"""Research Query: {query}

Web Search Results:
{search_results}

IMPORTANT: Provide a COMPLETE, COMPREHENSIVE, DETAILED research response. Do not truncate or stop mid-sentence. Ensure all sections are fully developed.

Please provide a thorough research response with the following structure:

## Summary
Provide a comprehensive 3-4 sentence overview of the topic with key insights.

## Key Findings
• Main finding 1 with detailed supporting information and context
• Main finding 2 with detailed supporting information and context  
• Main finding 3 with detailed supporting information and context
• Additional important findings with full explanations

## Detailed Analysis
Provide comprehensive, in-depth explanation with:
- Technical details and mechanisms
- Context and background information
- Examples, statistics, and data from search results
- Implications and significance
- Current state and future prospects

## Conclusion
Provide detailed summary of main takeaways, implications, and significance.

## Sources
List all relevant URLs and sources from the search results with brief descriptions.

CRITICAL: Complete ALL sections fully. Do not stop writing until you have provided comprehensive coverage of the topic. Write a thorough, professional response that addresses every aspect of the query:"""
        
        response = llm.generate(prompt)
        print("✅ Research complete!")
        
        return response
        
    except Exception as e:
        error_msg = f"❌ Research error: {str(e)}"
        print(error_msg)
        return error_msg
