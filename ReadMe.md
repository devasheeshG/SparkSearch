
## SQL (PostgreSQL)

### Table: `users`

- `id` (SERIAL PRIMARY KEY)
- `username` (VARCHAR(50) UNIQUE NOT NULL)
- `password_hash` (VARCHAR(255) NOT NULL)
- `created_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)

### Table: `files`

- `id` (SERIAL PRIMARY KEY)
- `user_id` (INT NOT NULL, FOREIGN KEY REFERENCES `users`(`id`))
- `file_path` (VARCHAR(255) NOT NULL)
- `file_name` (VARCHAR(255) NOT NULL)
- `file_type` (VARCHAR(50) NOT NULL)
- `page_count` (INT NOT NULL)
- `created_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)

### Table: `chunks`

- `id` (SERIAL PRIMARY KEY)
- `file_id` (INT NOT NULL, FOREIGN KEY REFERENCES `files`(`id`))
- `page_num` (INT NOT NULL)
- `text` (TEXT NOT NULL)
- `created_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)

## NoSQL (MongoDB)

### Collection: `chunk_data`

- `_id` (ObjectId)
- `chunk_id` (Int, FOREIGN KEY REFERENCES `chunks`(`id`))
- `title` (String)
- `text` (String)
- `created_at` (Date)
- `updated_at` (Date)

## Vector Database (Milvus)

### Collection: `embeddings`

- `id` (String, FOREIGN KEY REFERENCES `chunks`(`id`))
- `username` (String, FOREIGN KEY REFERENCES `users`(`username`))
- `embeddings` (Float[])
