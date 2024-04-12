# Path: backend/main.py
# Description: This is the main file that contains the FastAPI application.

import bcrypt, os
from dotenv import load_dotenv
from uuid import UUID, uuid4
from typing import List
from fastapi import FastAPI, Form, HTTPException, status, File, UploadFile
from fastapi.responses import JSONResponse, Response
from backend.database import Postgres, MongoDB, VectorDB
from backend.ingestion import extract_chunks_from_document, embed_chunks
from backend.utils.model import Chunk, Embedding, UploadedFile
load_dotenv('backend/.env')

app = FastAPI(
    title="SparkSearch Backend API",
    description="SparkSearch Backend API",
    version="0.0.1",
    docs_url='/api/docs',
    redoc_url='/api/redocs',
)

postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DATABASE"))
postgress.connect()
mongodb = MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE"))
mongodb.connect()
vectordb = VectorDB(uri=os.getenv("MILVUS_URI"), database_name=os.getenv("MILVUS_DATABASE"))
vectordb.connect()

@app.get("/")
async def root():
    return {"message": "Welcome to the SparkSearch API."}

@app.post("/api/auth/register")
async def register(username: str = Form(...), password: str = Form(...)):
    """Register a new user."""
    try:
        # Check if the user already exists in the database
        postgress.cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
        if postgress.cursor.fetchone():
            raise HTTPException(status_code=400, detail="User already exists, please login.")

        # Hash the password with a salt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Insert the user into the database
        postgress.cursor.execute(f"INSERT INTO users (username, password_hash, salt) VALUES ('{username}', '{hashed_password.decode('utf-8')}', '{salt.decode('utf-8')}')")

        return JSONResponse(content={"status": "success", "message": "User registered successfully."}, status_code=status.HTTP_201_CREATED)
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/auth/login")
async def login(username: str = Form(...), password: str = Form(...)):
    """Verify a user."""
    postgress.cursor.execute(f"SELECT id, password_hash, salt FROM users WHERE username='{username}'")
    result = postgress.cursor.fetchone()
    if result:
        user_id, hashed_password, salt = result
        rehashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        if rehashed_password.decode('utf-8') == hashed_password:
            return JSONResponse(content={"status": "success", "message": "User verified successfully.", "user_id": user_id}, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=400, detail="Invalid username or password.")

@app.post("/api/upload_file")
async def upload_document(file: UploadFile = File(...), path: str = Form(...), user_id: str = Form(...)):
    """
    Upload a single PDF, PowerPoint, or Word document and embed it into the vector database.
    """
    try:
        # Check if `user_id` exists in the database
        postgress.cursor.execute(f"SELECT * FROM users WHERE id='{user_id}'")
        if not postgress.cursor.fetchone():
            raise HTTPException(status_code=400, detail="User does not exist.")

        file_type = file.filename.split(".")[-1].lower()
        if file_type in ["pdf", "rtf"]:
            # Insert the file into the database
            if file_type == "pdf":
                import PyPDF2
                reader = PyPDF2.PdfReader(file.file)
                page_count = len(reader.pages)
            
            if file_type == "rtf":
                page_count = 0
        
            file_data = UploadedFile(
                user_id=user_id,
                file_path=path,
                file_name=file.filename,
                file_type=file_type,
                page_count=page_count
            )
            
            postgress.cursor.execute(f"INSERT INTO files (user_id, file_path, file_name, file_type, page_count) VALUES ('{file_data.user_id}', '{file_data.file_path}', '{file_data.file_name}', '{file_data.file_type}', '{file_data.page_count}') RETURNING id")
            file_data.id = postgress.cursor.fetchone()[0]
    
            chunks: List[Chunk] = await extract_chunks_from_document(file, file_data)
        #     embedding_data: List[Embedding] = await embed_chunks(chunks)
            
        #     for data in embedding_data:
        #         # Insert the chunk text into the MongoDB database
        #         inserted_id = mongodb.client.insert_one(
        #             collection_name=mongodb.collection_name,
        #             document=data.chunk.model_dump()
        #         ).inserted_id
                
        #         # Assign the inserted ID to data.id after converting it to a string
        #         data.id = str(inserted_id)
                
        #         # Insert the embeddings into the Milvus database
        #         vectordb.client.insert(
        #             collection_name=vectordb.collection_name,
        #             data={
        #                 "chunk_id": str(data.chunk._id),
        #                 "file_id": str(data.chunk.file_id),
        #                 "embeddings": data.embeddings
        #             }
        #         )

            return JSONResponse(content={"status": "success", "message": "Document uploaded and embedded successfully.", "file_id": str(file_data.id)}, status_code=status.HTTP_201_CREATED)
        
        else:
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF, PowerPoint, or Word document.")

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/delete_file")
async def delete_file(file_id: str = Form(...)):
    """
    Delete the document from the database.
    """
    try:
        postgress.cursor.execute(f"DELETE FROM files WHERE id='{file_id}'")
        mongodb.client.delete_many(collection_name=mongodb.collection_name, query={"file_id": file_id})
        vectordb.client.delete(collection_name=vectordb.collection_name, query={"file_id": file_id})
        return JSONResponse(content={"status": "success", "message": "Document deleted successfully."}, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/get_file_ids")
async def get_file_ids(user_id: str = Form(...)):
    """Get all the file IDs for the given user."""
    postgress.cursor.execute(f"SELECT id, file_path, file_name, file_type, page_count FROM files WHERE user_id='{user_id}'")
    file_ids = postgress.cursor.fetchall()
    return JSONResponse(content={"status": "success", "message": "File IDs retrieved successfully.", "file_ids": file_ids}, status_code=status.HTTP_200_OK)

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
