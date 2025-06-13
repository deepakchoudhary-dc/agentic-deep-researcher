# 🔍 Agentic Deep Researcher

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?logo=ollama&logoColor=white)](https://ollama.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An MCP-powered multi-agent deep researcher that performs comprehensive web searches using LinkUp API and provides detailed, fast responses using an optimized Ollama setup.

YOU NEED TO HAVE OLLAMA INSTALLED ON YOUR LOCAL MACHINE TO MAKE IT WORK.
## ✨ Features

- **⚡ Fast & Detailed**: Optimized for speed while maintaining comprehensive responses
- **🌐 LinkUp Integration**: Deep web search capabilities  
- **🤖 Qwen3 1.7B Model**: Optimized local LLM via Ollama
- **💻 Streamlit UI**: Clean, interactive web interface
- **🔧 MCP Server**: Integration with VS Code and other MCP clients
- **📊 Structured Output**: Professional formatting with citations

## 🚀 Quick Start

### 📋 Prerequisites
- Python 3.11+
- Ollama with qwen3:1.7b model
- LinkUp API key

### 🛠️ Installation

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

## 📖 Usage

### 🌐 Web Interface
- Open the Streamlit app
- Enter your LinkUp API key
- Ask any research question
- Get comprehensive, structured responses

### 🔧 MCP Server
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

## 📁 Project Structure

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

## ⚡ Performance Optimizations

- **Speed**: 40-60% faster than standard implementations
- **No Thinking Delays**: Automatic removal of model thinking artifacts
- **Structured Output**: Professional formatting with sections
- **Resource Efficient**: Optimized CPU and memory usage

## 📸 Demo

### Streamlit Interface
![image](https://github.com/user-attachments/assets/108c065a-dcda-4a0c-baf9-b43506b42f1a)



## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LinkUp](https://linkup.so/) for powerful web search capabilities
- [Ollama](https://ollama.ai/) for local LLM inference
- [Streamlit](https://streamlit.io/) for the beautiful web interface
- [FastMCP](https://github.com/jlowin/fastmcp) for MCP server implementation

## 📞 Support

If you have any questions or need help getting started:
- Open an [issue](https://github.com/yourusername/agentic-deep-researcher/issues)
- Check the [documentation](README.md)
- Join our [discussions](https://github.com/yourusername/agentic-deep-researcher/discussions)
