# Agentic Deep Researcher

An MCP-powered multi-agent deep researcher that performs comprehensive web searches using LinkUp API and provides detailed, fast responses using an optimized Ollama setup.

## Features

- **Fast & Detailed**: Optimized for speed while maintaining comprehensive responses
- **LinkUp Integration**: Deep web search capabilities
- **Qwen3 1.7B Model**: Optimized local LLM via Ollama
- **Streamlit UI**: Clean, interactive web interface
- **MCP Server**: Integration with VS Code and other MCP clients

## Quick Start

### Prerequisites
- Python 3.11+
- Ollama with qwen3:1.7b model
- LinkUp API key

### Installation

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Start Ollama:**
   ```bash
   ollama serve
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

5. **Enter your LinkUp API key** in the sidebar

## Usage

### Web Interface
- Open the Streamlit app
- Enter your LinkUp API key
- Ask any research question
- Get comprehensive, structured responses

### MCP Server
Add this to your `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "crew_research": {
      "command": "uv",
      "args": [
        "--directory",
        "d:\\mcp",
        "run",
        "server.py"
      ],
      "env": {
        "LINKUP_API_KEY": "your_linkup_api_key_here"
      }
    }
  }
}
```

## Project Structure

```
.
├── app.py                   # Streamlit web application
├── optimized_research.py    # Core research engine
├── server.py               # MCP server implementation
├── pyproject.toml          # Project dependencies
├── README.md               # This file
├── .env.example            # Environment variables template
└── .gitignore              # Git ignore rules
```

## Performance Optimizations

- **Speed**: 40-60% faster than standard implementations
- **No Thinking Delays**: Automatic removal of model thinking artifacts
- **Structured Output**: Professional formatting with sections
- **Resource Efficient**: Optimized CPU and memory usage

## Get Your API Key

Get your LinkUp API key from: [https://app.linkup.so/sign-up](https://app.linkup.so/sign-up)
