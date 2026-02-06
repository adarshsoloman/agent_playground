# Learning Notes - Local AI Agent with Ollama & LangChain

**Date:** February 7, 2026  
**Tutorial:** [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw&t=483s)  
**Channel:** Tech with Tim

---

## 🎯 What I Learned Today

### 1. **Ollama - Local LLM Runtime**
- Ollama allows you to run large language models **locally** on your machine
- No API costs, no internet required (after model download)
- Models used today:
  - `llama3.2` - Main LLM for generating responses
  - `mxbai-embed-large` - Embedding model for RAG

**Commands:**
```bash
ollama pull llama3.2              # Download the LLM
ollama pull mxbai-embed-large     # Download the embedding model
ollama list                        # List installed models
```

---

### 2. **LangChain Framework**

#### **Core Concepts:**

**a) LLM Wrapper**
```python
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="llama3.2")
```
- Connects to your local Ollama server (http://localhost:11434)
- Provides a standardized interface to interact with the LLM

**b) Prompt Templates**
```python
from langchain_core.prompts import ChatPromptTemplate

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
```
- Templates allow you to structure prompts with **placeholders** (`{reviews}`, `{question}`)
- Makes prompts reusable and dynamic
- Use `ChatPromptTemplate.from_template()` method (not direct instantiation)

**c) Chains - The Power of Piping**
```python
chain = prompt | model
```
- The **pipe operator (`|`)** creates a LangChain chain
- Means: "Take prompt → pass to model → get response"
- Chains can be extended: `prompt | model | parser | output_handler`

**d) Invoking Chains**
```python
result = chain.invoke({"reviews": [], "question": "What is the best pizza?"})
```
- Pass a dictionary with values for your template placeholders
- The chain processes the data through each component
- Returns the final result

---

### 3. **RAG (Retrieval-Augmented Generation)**

RAG = **Retrieval** + **Augmented** + **Generation**

#### **How It Works:**
1. **Load Data** - Read documents/reviews from CSV, PDFs, etc.
2. **Create Embeddings** - Convert text into vector representations
3. **Store in Vector DB** - Save embeddings for fast similarity search
4. **Retrieve Relevant Docs** - Find documents similar to the user's query
5. **Augment Prompt** - Inject retrieved docs into the LLM prompt
6. **Generate Response** - LLM creates an answer based on the context

#### **Implementation:**

```python
# 1. Load CSV data
df = pd.read_csv("realistic_restaurant_reviews.csv")

# 2. Create embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# 3. Create documents
documents = []
for i, row in df.iterrows():
    document = Document(
        page_content=row["Title"] + " " + row["Review"],
        metadata={"rating": row["Rating"], "date": row["Date"]},
        id=str(i)
    )
    documents.append(document)

# 4. Create vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory="./chroma_langchain_db",
    embedding_function=embeddings
)

# 5. Add documents to vector store
vector_store.add_documents(documents=documents, ids=ids)

# 6. Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Retrieve top 5 most relevant reviews
)

# 7. Use retriever in your chain
reviews = retriever.invoke(question)
result = chain.invoke({"reviews": reviews, "question": question})
```

---

### 4. **ChromaDB - Vector Database**
- Stores document embeddings
- Performs **similarity search** to find relevant documents
- Configuration:
  - `collection_name` - Name of your collection
  - `persist_directory` - Where to save the database
  - `embedding_function` - The embedding model to use

---

### 5. **Project Structure**

```
2_Local_AI_Agent-OLLAMA/
├── main.py                    # Main application with user interaction loop
├── vector.py                  # RAG setup (embeddings, vector store, retriever)
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Project configuration (IMPORTANT!)
├── .python-version           # Python version for UV
├── realistic_restaurant_reviews.csv  # Data source
└── chroma_langchain_db/      # Vector database storage (auto-created)
```

---

## ❌ Errors Encountered & Solutions

### **Error 1: Missing `langchain-core` Dependency**

**Error:**
```
ModuleNotFoundError: No module named 'langchain_core'
```

**Cause:**  
`langchain-ollama` depends on `langchain-core`, but it wasn't in `requirements.txt`

**Solution:**  
Added `langchain-core` to `requirements.txt`:
```text
langchain
langchain-core       # ← Added this
langchain-ollama
langchain-chroma
pandas
```

---

### **Error 2: Python 3.14 Incompatibility with Pydantic V1**

**Error:**
```
UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
pydantic.v1.errors.ConfigError: unable to infer type for attribute "chroma_server_nofile"
```

**Cause:**  
- Using **Python 3.14** (too new!)
- ChromaDB relies on **Pydantic V1**, which doesn't support Python 3.14+
- Python 3.14 introduced breaking changes that make older libraries incompatible

**Solution:**  
Switched to **Python 3.12**:

1. **Updated `pyproject.toml`:**
```toml
requires-python = ">=3.12,<3.14"  # Changed from ">=3.14"
```

2. **Pinned Python version:**
```bash
uv python pin 3.12
```

3. **Recreated virtual environment:**
```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

**Key Lesson:**  
- Python 3.14 is **very new** and many packages haven't caught up
- For LangChain/ChromaDB projects, use **Python 3.11 or 3.12**
- Always check library compatibility before using bleeding-edge Python versions

---

### **Error 3: Typos in `vector.py`**

**Errors Found:**

| Line | Error | Fix |
|------|-------|-----|
| 4 | `from langchain_core.documents import documents` | `import Document` (capital D) |
| 20 | `df.iterows()` | `df.iterrows()` (missing 'r') |
| 33 | `persist_directory="db_location"` | `persist_directory=db_location` (remove quotes - it's a variable!) |
| 41 | `as_retriver()` | `as_retriever()` (correct spelling) |

**Lesson:**  
- Pay attention to **capitalization** in class names
- **String literals vs variables** - quotes make a difference!
- **Spelling matters** - `retriever` not `retriver`

---

### **Error 4: UV Recreating Venv with Wrong Python Version**

**Error:**
```
Using CPython 3.14.2 interpreter at: C:\Python314\python.exe
Removed virtual environment at: .venv
```

**Cause:**  
- `.python-version` file was set to `3.14`
- `pyproject.toml` had `requires-python = ">=3.14"`
- `uv run` reads these files and recreates the venv with Python 3.14

**Solution:**
1. Updated `pyproject.toml` to `requires-python = ">=3.12,<3.14"`
2. Ran `uv python pin 3.12` to update `.python-version`
3. Recreated venv with correct Python version

**Lesson:**  
Both `.python-version` and `pyproject.toml` control which Python version UV uses!

---

## 📌 Important Concepts

### **1. The Pipe Operator in LangChain**
```python
chain = prompt | model
```
- This is **NOT** a bitwise OR operator
- In LangChain, `|` means "pipe the output of the left into the right"
- Equivalent to functional composition: `model(prompt(input))`

---

### **2. `pyproject.toml` - Modern Python Project Configuration**

#### **What It Does:**
- Central configuration file for modern Python projects
- Replaces/supplements `setup.py` and other config files
- Used by tools like `uv`, `pip`, `poetry`, `hatch`

#### **Key Sections:**
```toml
[project]
name = "2-local-ai-agent-ollama"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12,<3.14"  # Python version constraint
dependencies = [
    "pandas>=3.0.0",
]
```

#### **Why It's Important:**
- **Python version control** - Ensures correct Python version is used
- **Dependency management** - More powerful than `requirements.txt`
- **Project metadata** - Name, version, description for publishing
- **Tool configuration** - Can configure pytest, black, ruff, etc.

#### **`pyproject.toml` vs `requirements.txt`:**

| Feature | `pyproject.toml` | `requirements.txt` |
|---------|------------------|-------------------|
| Modern standard | ✅ | ❌ Legacy |
| Python version control | ✅ | ❌ |
| Project metadata | ✅ | ❌ |
| Build system config | ✅ | ❌ |
| Tool configs | ✅ | ❌ |
| Simple deps list | ✅ | ✅ |

**Modern best practice:** Use `pyproject.toml` for everything, keep `requirements.txt` for backwards compatibility if needed.

---

### **3. UV - Fast Python Package Manager**

#### **Why UV is Better:**
- **10-100x faster** than pip
- Written in Rust
- Better dependency resolution
- Integrated virtual environment management

#### **Key Commands:**
```bash
# Create virtual environment
uv venv --python 3.12

# Install dependencies
uv pip install -r requirements.txt

# Run scripts (auto-manages venv)
uv run main.py

# Manage Python versions
uv python pin 3.12

# List installed packages
uv pip list
```

---

### **4. Document Class in LangChain**
```python
from langchain_core.documents import Document

document = Document(
    page_content="The actual text content",  # Main content
    metadata={"key": "value"},               # Additional data
    id="unique_id"                           # Unique identifier
)
```
- `page_content` - The actual text to embed/search
- `metadata` - Extra information (rating, date, author, etc.)
- `id` - Unique identifier for the document

---

### **5. Embeddings - Turning Text into Numbers**
- Embeddings convert text into **vectors** (lists of numbers)
- Similar text → similar vectors
- Vector databases use these to find relevant documents via **cosine similarity**
- Example: "pizza" and "pasta" have more similar embeddings than "pizza" and "car"

---

## 🎓 Key Takeaways

### **Code Quality (Tech with Tim Style):**
✅ **Clean and concise** - No unnecessary complexity  
✅ **Well-structured** - Logical separation of concerns  
✅ **Easy to follow** - Clear variable names and flow  
✅ **Practical** - Gets to the point, no fluff  

### **Good Code vs Bad Code:**
- **Good:** Clear intent, self-documenting, modular
- **Bad:** Confusing variable names, monolithic functions, unclear structure

### **Tech with Tim's Teaching:**
- Focuses on **practical implementation**
- Code is **to the point** - no over-engineering
- Great balance of **theory and practice**

---

## 🚀 What's Next?

Now that I understand the basics, I can:

1. **Expand this agent:**
   - Add more data sources (PDFs, websites)
   - Implement tool calling for agents
   - Add memory/conversation history

2. **Build custom applications:**
   - Personal document Q&A system
   - Code documentation assistant
   - Research paper analyzer

3. **Explore more LangChain:**
   - Agent frameworks
   - Multiple chains
   - Custom tools and functions

4. **Try different models:**
   - `codellama` for coding tasks
   - `mistral` for general chat
   - `phi3:mini` for lightweight tasks

---

## 📚 Resources

### Documentation
- [Ollama Docs](https://ollama.ai/docs)
- [LangChain Docs](https://python.langchain.com/)
- [ChromaDB Docs](https://docs.trychroma.com/)

### Models
- [Ollama Model Library](https://ollama.ai/library)
- Browse available models and their sizes

### Related Topics to Learn
- Vector databases (Pinecone, Weaviate, FAISS)
- Prompt engineering
- Agent frameworks (LangGraph, AutoGPT)
- Fine-tuning local models

---

## 💡 Final Thoughts

**What worked well:**
- Ollama made running LLMs locally **super easy**
- LangChain's chain abstraction is **powerful and clean**
- RAG implementation was **straightforward** with ChromaDB
- UV made package management **blazing fast**

**Challenges faced:**
- Python version compatibility (3.14 vs 3.12)
- Understanding `pyproject.toml` importance
- Catching typos in variable names
- Learning the LangChain syntax

**Biggest lesson:**
Clean, well-structured code (like Tech with Tim's) makes learning so much easier. No over-engineering, just practical implementation that **works**.

---

**Session completed successfully! 🎉**
