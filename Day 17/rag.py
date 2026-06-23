from PyPDF2 import PdfReader
from docx import Document
# from langchain_core.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv() 
api_key = os.environ.get("GROQ_API_KEY")


#load documents

def get_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_docx(path):
    doc = Document(path)
    paragraphs = []
    for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                paragraphs.append(text)
    content = "\n\n".join(paragraphs)
    return content

def get_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
# chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# embedding 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vector database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def process_documents(path):
    if path.endswith(".pdf"):
        text = get_pdf(path)
    elif path.endswith(".docx"):
        text = get_docx(path)
    elif path.endswith(".txt"):
        text = get_txt(path)
    else:
        raise ValueError("Only pdf, docx and txt files are supported")

    chunks = splitter.split_text(text)
    filename = os.path.basename(path)
    metadata = []
    for _ in chunks:
        metadata.append({
            "source": filename,
            "uploaded": str(datetime.now())
        })
    vectorstore.add_texts(
        texts=chunks,
        metadatas=metadata
    )
    return len(chunks)

llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=api_key,temperature=0.5)

history = []

def ask_query(query):
    docs = vectorstore.similarity_search(query,k=3)
    context = "\n".join(
        doc.page_content
        for doc in docs
    )
    prompt = f"""
    You are an assistant for question-answering tasks. Answer using only the context. If you don't know the answer then just say you don't know.
    Context:  {context}
    Question: {query}
    """
    response = llm.invoke(prompt)
    answer = response.content
    history.append({
        "question":query,
        "answer": response.content})
    return {
        "answer": answer,
        "sources": [
            doc.metadata["source"]
            for doc in docs
        ]
    }


def get_history():
    return history