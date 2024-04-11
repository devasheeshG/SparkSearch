# Path: backend/ingestion/model.py
# Description: This file contains the Pydantic model for the chunk object.

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import List

# Postgres models
class User(BaseModel):
    id: UUID    # Automatically generated UUID by Postgres
    username: str
    password_hash: str
    salt: str

class UploadedFile(BaseModel):
    id: UUID    # Automatically generated UUID by Postgres
    user_id: UUID
    file_path: str
    file_name: str
    file_type: str
    page_count: int

# MongoDB models
class Chunk(BaseModel):
    _id: UUID   # Automatically generated UUID by MongoDB
    file_id: UUID
    page_num: int
    title: str
    text: str

# Milvus models
class Embedding(BaseModel):
    chunk: Chunk
    embeddings: List[float]
