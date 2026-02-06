# Local AI Agent with Python

Building a local AI agent using **Ollama**, **LangChain**, and **RAG (Retrieval-Augmented Generation)** - following the Tech with Tim tutorial.

## 📚 Learning Source

**YouTube Tutorial:** [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw&t=483s)  
**Channel:** Tech with Tim  
**Date:** February 7, 2026  
**Status:** ✅ **COMPLETED**

---

## 🎯 Learning Objectives

- [x] Understand the fundamentals of AI agents
- [x] Learn to work with **Ollama** for local LLM deployment
- [x] Master **LangChain** framework for agent development
- [x] Implement **RAG (Retrieval-Augmented Generation)** patterns
- [x] Build a fully functional local AI agent from scratch

---

## 🛠️ Technologies & Tools

### Core Stack
- **Python** - Primary programming language
- **Ollama** - Local LLM runtime (run models locally without API costs)
- **LangChain** - Framework for building LLM applications
- **RAG** - Retrieval-Augmented Generation for context-aware responses

### Key Concepts to Learn
- Agent architecture and design patterns
- Vector databases and embeddings
- Prompt engineering
- Memory and context management
- Tool/function calling with agents

---

## 📋 Prerequisites

### Required
- ✅ Python 3.12 installed (Note: Python 3.14 has compatibility issues with ChromaDB)
- ✅ Basic Python knowledge
- ✅ Ollama installed

### Installed Dependencies
- `langchain` - LangChain framework
- `langchain-core` - Core LangChain functionality
- `langchain-ollama` - Ollama integration for LangChain
- `langchain-chroma` - ChromaDB integration for LangChain
- `pandas` - Data manipulation library

---

## 🚀 Setup Instructions

### 1. Install Ollama
```bash
# Download and install from: https://ollama.ai
# Verify installation
ollama --version
```

### 2. Pull Required Models
```bash
# Main LLM for responses
ollama pull llama3.2

# Embedding model for RAG
ollama pull mxbai-embed-large
```

### 3. Set Up Python Environment
```bash
# Create virtual environment with Python 3.12
uv venv --python 3.12

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### 4. Run the Application
```bash
# Run the agent
uv run main.py

# Or with activated venv
python main.py
```

---

## 📁 Project Structure

```
2_Local_AI_Agent-OLLAMA/
├── README.md                                  # Project documentation
├── notes.md                                   # Detailed learning notes
├── requirements.txt                           # Python dependencies
├── pyproject.toml                            # Project configuration
├── .python-version                           # Python version (3.12)
├── uv.lock                                   # UV lock file
├── main.py                                   # Main application with user interaction
├── vector.py                                 # RAG implementation (embeddings, vector store)
├── realistic_restaurant_reviews.csv          # Sample data
├── chroma_langchain_db/                      # ChromaDB vector database (auto-created)
└── .venv/                                    # Virtual environment
```

---

## 📝 Learning Notes

### What I Built
A **local AI agent** that:
- Uses **Ollama** to run LLMs locally (llama3.2)
- Implements **RAG (Retrieval-Augmented Generation)** with ChromaDB
- Loads restaurant reviews from CSV
- Creates embeddings with `mxbai-embed-large`
- Retrieves relevant reviews based on questions
- Generates contextual responses using LangChain

### Key Concepts Learned
- **LangChain chains** - Using the pipe operator (`|`)
- **Prompt templates** - Dynamic prompt construction
- **RAG architecture** - Retrieval + Augmented + Generation
- **Vector databases** - ChromaDB for similarity search
- **pyproject.toml** - Modern Python project configuration
- **Python version compatibility** - 3.14 vs 3.12 issues

📚 **Detailed notes:** See [notes.md](./notes.md) for comprehensive documentation of concepts, errors, and solutions.

---

## 🚧 Current Progress

- [x] Created project structure
- [x] Installed Ollama
- [x] Downloaded llama3.2 and mxbai-embed-large models
- [x] Installed LangChain and dependencies
- [x] Completed tutorial
- [x] Built RAG-powered chatbot
- [x] Implemented vector database with ChromaDB
- [x] Created comprehensive learning notes

---

## � Resources & References

### Official Documentation
- [Ollama Documentation](https://ollama.ai/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain RAG Guide](https://python.langchain.com/docs/use_cases/question_answering/)
- [ChromaDB Documentation](https://docs.trychroma.com/)

### Additional Learning
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Ollama Models Library](https://ollama.ai/library)
- [UV Package Manager](https://github.com/astral-sh/uv)

---

## 💡 Next Steps & Project Ideas

Now that the tutorial is complete, potential projects to build:
1. **Personal document Q&A system** - RAG with your own PDFs/notes
2. **Code documentation assistant** - Analyze and explain codebases
3. **Research paper analyzer** - Summarize academic papers
4. **Custom knowledge base chatbot** - Build domain-specific agents
5. **Multi-document comparison tool** - Compare and contrast documents

### Future Learning Topics
- LangChain agents with tool calling
- LangGraph for complex workflows
- Fine-tuning local models
- Building custom embeddings
- Advanced prompt engineering

---

## � Issues & Solutions

See [notes.md](./notes.md) for detailed documentation of all errors encountered and their solutions, including:
- Missing `langchain-core` dependency
- Python 3.14 compatibility issues with ChromaDB
- Typos in imports and method names
- UV virtual environment recreation issues

---

**Tutorial Completed! 🎉**  
For detailed learning notes, code explanations, and troubleshooting guide, see [notes.md](./notes.md)
