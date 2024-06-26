# Path: backend/ingestion/__init__.py
# Description: This file contains the code for extracting the chunks from the document.

from fastapi import File
from backend.utils.model import Chunk, Embedding
from typing import List
from tempfile import NamedTemporaryFile
from backend.utils.model import UploadedFile, Chunk, Embedding

async def extract_chunks_from_document(file: File, file_data: UploadedFile) -> List[Chunk]:
    ## PDF
    if file_data.file_type == "pdf":
        from llama_index.readers.file import PDFReader
        reader = PDFReader(return_full_document=True)
        with NamedTemporaryFile(delete=True, suffix='.pdf') as temp_file:
            temp_file.write(await file.read())
            document = reader.load_data(temp_file.name)
            
            if len(document) == 0:
                raise ValueError("No text found in the document.")
            if len(document) > 1:
                raise NotImplementedError("Multiple pages are not supported.")
            
            return [Chunk(file_id=file_data.id, page_num=0, title=file_data.file_name, text=document[0].text)]
    
    ## RTF
    elif file_data.file_type == "rtf":
        from striprtf.striprtf import rtf_to_text
        with NamedTemporaryFile(delete=True, suffix='.rtf') as temp_file:
            temp_file.write(await file.read())
            
            with open(temp_file.name, 'r') as f:
                file_content = f.read()
        
            return [Chunk(file_id=file_data.id, page_num=0, title=file_data.file_name, text=rtf_to_text(file_content))]

async def embed_chunks(chunks: List[Chunk]) -> List[Embedding]:
    from openai import OpenAI
    import os
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    embeddings = []
    for chunk in chunks:
        embedding = client.embeddings.create(input = [chunk.text], model='text-embedding-3-large').data[0].embedding
        embeddings.append(Embedding(chunk=chunk, embeddings=embedding))
    return embeddings
