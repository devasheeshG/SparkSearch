# Path: backend/database/setup.py
# Description: This file contains the code to setup tables in all the databases.

def setup_postgress_database_tables(self) -> None:
    self.execute_query(
        """
        CREATE TABLE IF NOT EXISTS users (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    self.execute_query(
        """
        CREATE TABLE IF NOT EXISTS files (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            user_id UUID NOT NULL REFERENCES users(id),
            file_path VARCHAR(255) NOT NULL,
            file_name VARCHAR(255) NOT NULL,
            file_type VARCHAR(50) NOT NULL,
            page_count INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    self.execute_query(
        """
        CREATE TABLE IF NOT EXISTS chunks (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            file_id UUID NOT NULL REFERENCES files(id),
            page_num INT NOT NULL,
            text TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

