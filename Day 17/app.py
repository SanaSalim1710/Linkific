from fastapi import FastAPI
from fastapi import UploadFile, File
from rag import process_documents
from rag import ask_query
from rag import get_history
import os
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"data":"test"}

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    supported = [".pdf",".docx",".txt"]
    # split into root path [0] and file extension [1]
    extension = os.path.splitext(file.filename)[1]
    if extension not in supported:
        return {
            "error":"Only pdf,txt and docx files are supported"
        }
    save_path = f"uploads/{file.filename}"
    contents = await file.read()
    with open(save_path, "wb") as f:
        f.write(contents)
    chunk_count = process_documents(save_path)
    return {
        "message":"Uploaded",
        "chunks": chunk_count
    }

@app.delete("/document/{filename}")
def delete_document(filename):
    path = f"uploads/{filename}"
    if os.path.exists(path):
        os.remove(path)
        return {"message":"Deleted"}
    return {"error":"File not found"}

@app.get("/documents")
def get_documents():
    return os.listdir("uploads")

history = []
@app.post("/query")
def query(data: Query):
    result = ask_query(data.question)
    return result

@app.get("/history")
def history():
    return get_history()