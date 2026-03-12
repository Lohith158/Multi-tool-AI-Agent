# Multi-Tool AI Agent

A locally running AI agent built with LangChain and Ollama that combines multiple tools — web search, document retrieval (RAG), Wikipedia search, and a calculator — with a Gradio chat interface. The agent uses the ReAct (Reasoning + Acting) framework to decide which tool to use based on the user's query.

---

## Features

- **Web Search** — searches the internet in real time using DuckDuckGo
- **Document Search (RAG)** — retrieves answers from local PDF documents using semantic search via ChromaDB and HuggingFace embeddings
- **Wikipedia Search** — fetches in-depth topic summaries from Wikipedia
- **Calculator** — evaluates mathematical expressions
- **Gradio Chat UI** — a clean browser-based chat interface to interact with the agent
- **Fully Local** — runs entirely on your machine using Ollama with Llama 3.2, no paid API required

---

## Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.2 via Ollama |
| Agent Framework | LangChain ReAct |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Web Search | DuckDuckGo (ddgs) |
| UI | Gradio |
| Backend | Python |

---

## Project Structure

```
AI_AGENT/
├── agent.py        # Agent logic, tools, and LLM configuration
├── app.py          # Gradio UI and entry point
├── RAG.pdf         # Sample document for document search tool
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com) installed and running locally
- Llama 3.2 model pulled via Ollama

---

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/AI_AGENT.git
cd AI_AGENT
```

**2. Install dependencies**

```bash
pip install langchain langchain-classic langchain-community langchain-ollama
pip install langchain-huggingface langchain-chroma
pip install langchain-text-splitters gradio ddgs wikipedia
```

**3. Pull the Llama 3.2 model using Ollama**

```bash
ollama pull llama3.2
```

**4. Add your PDF document**

Place any PDF file in the project root and update the filename in `agent.py`:

```python
pdf = PyPDFLoader("your-document.pdf")
```

**5. Run the application**

```bash
python app.py
```

**6. Open the UI**

Visit `http://127.0.0.1:7860` in your browser.

---

## How It Works

The agent uses the ReAct (Reasoning + Acting) pattern. For every user message, it follows this loop:

1. **Thought** — decides what needs to be done
2. **Action** — selects the appropriate tool
3. **Observation** — reads the tool's output
4. **Repeat** until a final answer is reached

The agent automatically selects the right tool based on the nature of the question. Math questions go to the calculator, document-specific questions use RAG, general knowledge uses Wikipedia, and current events use web search.

---

## Example Queries

| Query | Tool Used |
|---|---|
| "What is 125 multiplied by 8?" | Calculator |
| "What is the latest news about AI?" | Web Search |
| "Explain quantum computing" | Wikipedia |
| "Summarize the uploaded document" | Document Search (RAG) |

---

## Key Concepts Demonstrated

- LangChain ReAct agent with custom tools
- Retrieval Augmented Generation (RAG) pipeline
- Local LLM inference using Ollama
- Semantic search with vector embeddings and ChromaDB
- Building AI applications with Gradio

---

## Author

Lohith G  
AI/ML Student  
[GitHub](https://github.com/Lohith158)  
[LinkedIn](https://linkedin.com/in/lohith-g-58680b2a6/)
