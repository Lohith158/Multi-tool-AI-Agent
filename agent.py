from langchain_ollama import OllamaLLM
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain_classic import hub
from ddgs import DDGS
import wikipedia
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Put brain to AGENT (LLM)
llm = OllamaLLM(model="llama3.2")

# Load documents
pdf = PyPDFLoader("RAG.pdf")
documents = pdf.load()

# Split the document
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
chunks = splitter.split_documents(documents)

# Covert text into embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store chunks in CromaDB
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

# Create a 1st tool
@tool
def calculate(expression: str) -> str:
    "Useful for solving math calculations. Input should be a math expression like '2 + 2'."
    result = eval(expression)
    return result

# Create a 2nd tool
@tool
def search(query: str) -> str:
    "Useful for searching relvant information. Input should be a query like 'what is latest news about AI Agents?'"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
        return str(results)
    
@tool
def WikiSearch(query: str) -> str:
    "Useful for deep search about particular topic. Input should be like 'what is mitochondria?'"
    return wikipedia.summary(query, sentences=5)

@tool
def SearchDocuments(query: str) -> str:
    "Useful when user ask queries from his local pdf/documents. Input be like 'summarize the pdf i uploaded'"
    results = vectorstore.similarity_search(query)
    context = " ".join([doc.page_content for doc in results])
    return context

    
# Handover toolbox to agent and pull the ReAct prompt from LangChain hub
tools = [calculate, search, WikiSearch, SearchDocuments]
prompt = hub.pull("hwchase17/react")

# Create Agent
agent = create_react_agent(llm, tools, prompt)

# Create Agent executer
executer = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=20, handle_parsing_errors=True)

