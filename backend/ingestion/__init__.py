# Path: backend/ingestion/__init__.py
# Description: This file contains the code for extracting the chunks from the document.

from fastapi import File
from .model import Chunk, Embedding
from typing import List


async def extract_chunks_from_document(file: File) -> List[Chunk]:
    raise NotImplementedError("`extract_chunks_from_document` function is not implemented.")

async def embed_chunks(chunks: List[Chunk]) -> List[Embedding]:
    raise NotImplementedError("`embed_chunks` function is not implemented.")