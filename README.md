# 🤖 Agent Playground

A collection of AI agent experiments and projects exploring the capabilities of various frameworks, models, and architectures.

## 📂 Projects

### [1_My_first-agent](./1_My_first-agent)
My first exploration into building AI agents. This project covers the fundamentals of agent creation, tool usage, and LLM integration.

**Key Features:**
- Basic agent implementation with custom tools
- Environment-based configuration
- LangChain integration

### [2_Local_AI_Agent-OLLAMA](./2_Local_AI_Agent-OLLAMA)
A local AI agent powered by Ollama, featuring vector database integration for RAG (Retrieval-Augmented Generation) capabilities.

**Key Features:**
- Runs completely offline with Ollama models
- ChromaDB vector store for document retrieval
- Restaurant reviews dataset for testing
- RAG implementation with LangChain

## 🚀 Getting Started

Each project contains its own README with specific setup instructions. Generally, you'll need:

```bash
# Navigate to a project
cd <project-folder>

# Create virtual environment (using uv or venv)
uv venv  # or python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt  # or pip install -r requirements.txt
```

## 🛠️ Tech Stack

- **Python 3.x** - Core programming language
- **LangChain** - Agent framework and orchestration
- **Ollama** - Local LLM inference
- **ChromaDB** - Vector database for embeddings
- **UV** - Fast Python package installer and resolver

## 📚 Learning Resources

This repository serves as my learning journey in AI agent development. Each project builds upon previous concepts and explores new techniques.

### Topics Explored:
- ✅ Basic agent architecture
- ✅ Tool creation and integration
- ✅ Local LLM deployment with Ollama
- ✅ Vector databases and RAG
- 🔄 Multi-agent systems (coming soon)
- 🔄 Agent memory and state management (coming soon)

## 🤝 Contributing

This is a personal learning repository, but feel free to:
- Open issues for suggestions
- Fork and experiment
- Share improvements via PRs

## 📝 Notes

- Each project maintains its own virtual environment
- API keys and sensitive data are stored in `.env` files (not tracked in git)
- Check individual project READMEs for specific requirements

## 📄 License

MIT License - Feel free to use this code for learning and experimentation!

---

**Happy Agent Building! 🚀**
