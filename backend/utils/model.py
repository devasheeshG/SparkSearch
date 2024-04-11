# Path: backend/ingestion/model.py
# Description: This file contains the Pydantic model for the chunk object.

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4
from typing import List

class User(BaseModel):
    id: UUID = uuid4()
    username: str
    password_hash: str
    created_at: datetime
    updated_at: datetime

class File(BaseModel):
    id: UUID = uuid4()
    user_id: UUID
    file_path: str
    file_name: str
    file_type: str
    page_count: int
    created_at: datetime
    updated_at: datetime

class Chunk(BaseModel):
    id: UUID = uuid4()
    file_id: UUID
    page_num: int
    text: str
    created_at: datetime
    updated_at: datetime

class ChunkData(BaseModel):
    _id: UUID = uuid4()
    chunk_id: UUID
    title: str
    text: str
    created_at: datetime
    updated_at: datetime

class Embedding(BaseModel):
    id: UUID = uuid4()
    username: str
    embeddings: List[float]
