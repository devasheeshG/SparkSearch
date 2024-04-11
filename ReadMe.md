## PostgreSQL Database Structure

### Table: `users`
- **Columns**:
  - `id` (UUID): Unique identifier for the user.
  - `username` (String): Username chosen by the user.
  - `password_hash` (String): Hashed password of the user.
  - `salt` (String): Salt used to hash the password.

### Table: `files`
- **Columns**:
  - `id` (UUID): Unique identifier for the file.
  - `user_id` (UUID): Foreign key referencing the `id` column in the `users` table, representing the user who uploaded the file.
  - `file_path` (String): Path to the uploaded file.
  - `file_name` (String): Name of the uploaded file.
  - `file_type` (String): Type of the file (e.g., PDF, TXT).
  - `page_count` (Integer): Number of pages in the file.

## MongoDB Database Structure

### Collection: `chunk_data`
- **Fields**:
  - `_id` (UUID): Unique identifier for the chunk.
  - `file_id` (UUID): Foreign key referencing the `id` column in the PostgreSQL `files` table, representing the file to which the chunk belongs.
  - `page_num` (Integer): Page number of the chunk within the file.
  - `title` (String): Title of the chunk (if any).
  - `text` (String): Text content of the chunk.

## Milvus Database Structure

### Collection: `embeddings`
- **Fields**:
  - `chunk_id` (UUID): Unique identifier for the embedding.
  - `file_id` (UUID): Foreign key referencing the `id` column in the PostgreSQL `files` table, representing the file to which the embedding belongs.
  - `embeddings` (List of Floats): List of floating-point values representing the embedding vector.
