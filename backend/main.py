# Path: backend/main.py
# Description: This is the main file that contains the FastAPI application.

import bcrypt, os
from dotenv import load_dotenv
from typing import List
from fastapi import FastAPI, Form, HTTPException, status, File, UploadFile
from database import Postgres, MongoDB, VectorDB
from ingestion import extract_chunks_from_document, embed_chunks
from ingestion.model import Chunk, Embedding
load_dotenv()

app = FastAPI(
    title="SparkSearch Backend API",
    description="SparkSearch Backend API",
    version="0.0.1",
    docs_url=None,
    redoc_url=None,
)

postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DB"))
mongodb = MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE"))
vectordb = VectorDB()

@app.post("/api/auth/register")
async def register(username: str = Form(...), password: str = Form(...)):
    """Register a new user."""
    # Check if the user already exists in the database
    postgress.execute(f"SELECT * FROM users WHERE username='{username}'")
    if postgress.cursor.fetchone():
        raise HTTPException(status_code=400, detail="User already exists.")

    # Hash the password with a salt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the user into the database
    postgress.execute(f"INSERT INTO users (username, password_hash, salt) VALUES ('{username}', '{hashed_password.decode('utf-8')}', '{salt.decode('utf-8')}')")

    return {"status": "success", "message": "User registered successfully."}, status.HTTP_201_CREATED

@app.post("/api/auth/login")
async def verify(username: str = Form(...), password: str = Form(...)):
    """Verify a user."""
    postgress.execute(f"SELECT password_hash, salt FROM users WHERE username='{username}'")
    result = postgress.cursor.fetchone()
    if result:
        hashed_password, salt = result
        rehashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        if rehashed_password.decode('utf-8') == hashed_password:
            return {"status": "success", "message": "User verified successfully."}, status.HTTP_200_OK

    raise HTTPException(status_code=400, detail="Invalid username or password.")

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...), path: str = Form(...), username: str = Form(...)):
    """
    Upload a single PDF, PowerPoint, or Word document and embed it into the vector database.
    """
    file_type = file.filename.split(".")[-1].lower()
    if file_type in ["pdf", "ppt", "pptx", "doc", "docx"]:
        chunks: List[Chunk] = await extract_chunks_from_document(file, path, file_type)
        embeddings: List[Embedding] = await embed_chunks(chunks)
        
        for chunk, embedding in zip(chunks, embeddings):
            with MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE")) as db:
                db.insert_one("chunks", chunk.model_dump())
                
            with VectorDB() as db:
                db.insert_one("embeddings", embedding.model_dump())
        
        return {"status": "success", "message": "Document uploaded and embedded successfully."}
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="192.168.0.253", 
        port=8000, 
        reload=True, 
        reload_dirs=["backend"], 
        debug=True
    )
