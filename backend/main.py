# Path: backend/main.py
# Description: This is the main file that contains the FastAPI application.

import bcrypt, os
from dotenv import load_dotenv
from uuid import UUID
from typing import List
from fastapi import FastAPI, Form, HTTPException, status, File, UploadFile
from backend.database import Postgres, MongoDB, VectorDB
from backend.ingestion import extract_chunks_from_document, embed_chunks
from backend.utils.model import Chunk, Embedding, UploadedFile
load_dotenv('backend/.env')

app = FastAPI(
    title="SparkSearch Backend API",
    description="SparkSearch Backend API",
    version="0.0.1",
    docs_url=None,
    redoc_url=None,
)

postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DB"))
mongodb = MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE"))
vectordb = VectorDB(uri=os.getenv("MILVUS_URI"), database_name=os.getenv("MILVUS_DATABASE"))

@app.post("/api/auth/register")
async def register(username: str = Form(...), password: str = Form(...)):
    """Register a new user."""
    # Check if the user already exists in the database
    postgress.execute(f"SELECT * FROM users WHERE username='{username}'")
    if postgress.cursor.fetchone():
        raise HTTPException(status_code=400, detail="User already exists, please login.")

    # Hash the password with a salt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the user into the database
    postgress.execute(f"INSERT INTO users (username, password_hash, salt) VALUES ('{username}', '{hashed_password.decode('utf-8')}', '{salt.decode('utf-8')}')")

    return {"status": "success", "message": "User registered successfully."}, status.HTTP_201_CREATED

@app.post("/api/auth/login")
async def verify(username: str = Form(...), password: str = Form(...)):
    """Verify a user."""
    postgress.execute(f"SELECT id, password_hash, salt FROM users WHERE username='{username}'")
    result = postgress.cursor.fetchone()
    if result:
        user_id, hashed_password, salt = result
        rehashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        if rehashed_password.decode('utf-8') == hashed_password:
            return {"status": "success", "message": "User verified successfully.", "id": user_id}, status.HTTP_200_OK

    raise HTTPException(status_code=400, detail="Invalid username or password.")

@app.post("/api/upload_file")
async def upload_document(file: UploadFile = File(...), path: str = Form(...), user_id: str = Form(...)):
    """
    Upload a single PDF, PowerPoint, or Word document and embed it into the vector database.
    """
    file_type = file.filename.split(".")[-1].lower()
    if file_type in ["pdf"]:
        # Insert the file into the database
        if file_type == "pdf":
            import PyPDF2
            pdf = PyPDF2.PdfFileReader(file.file)
            page_nums = pdf.getNumPages()
        
        file_data = UploadedFile(
            id=None,
            user_id=user_id,
            file_path=path,
            file_name=file.filename,
            file_type=file_type,
            page_count=page_nums
        )
        
        postgress.execute(f"INSERT INTO files (user_id, file_path, file_name, file_type, page_count) VALUES ('{file_data.user_id}', '{file_data.file_path}', '{file_data.file_name}', '{file_data.file_type}', '{file_data.page_count}') RETURNING id")
        file_data.id = postgress.cursor.fetchone()[0]
 
        chunks: List[Chunk] = await extract_chunks_from_document(file, file_data.id)
        embedding_data: List[Embedding] = await embed_chunks(chunks)
        
        for data in embedding_data:
            # Insert the chunk text into the MongoDB database
            inserted_id = mongodb.client.insert_one(
                collection_name=mongodb.collection_name,
                document=data.chunk.model_dump()
            ).inserted_id
            
            # Assign the inserted ID to data.id after converting it to a string
            data.id = str(inserted_id)
            
            # Insert the embeddings into the Milvus database
            vectordb.client.insert(
                collection_name=vectordb.collection_name,
                data={
                    "chunk_id": str(data.chunk._id),
                    "file_id": str(data.chunk.file_id),
                    "embeddings": data.embeddings
                }
            )
            
        return {"status": "success", "message": "Document uploaded and embedded successfully.", "file_id": file_data.id}, status.HTTP_201_CREATED
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

@app.post("/api/delete_file")
async def delete_file(file_id: str = Form(...)):
    """
    Delete the document from the database.
    """
    try:
        postgress.execute(f"DELETE FROM files WHERE id='{file_id}'")
        mongodb.client.delete_many(collection_name=mongodb.collection_name, query={"file_id": file_id})
        vectordb.client.delete(collection_name=vectordb.collection_name, query={"file_id": file_id})
        return {"status": "success", "message": "Document deleted successfully."}, status.HTTP_200_OK
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/get_file_ids")
async def get_file_ids(user_id: str = Form(...)):
    """Get all the file IDs for the given user."""
    postgress.execute(f"SELECT id, file_path, file_name, file_type, page_count FROM files WHERE user_id='{user_id}'")
    file_ids = postgress.cursor.fetchall()
    return {"status": "success", "message": "File IDs retrieved successfully.", "file_ids": file_ids}, status.HTTP_200_OK

@app.post("/api/search")
async def search(query: str = Form(...), included_file_ids: List[str] = Form(...)):
    """
    Search the vector database for the query for the given user.
    """
    pass

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
