# Path: backend/database/postgress.py
# Description: This file contains the code to connect to a Postgres database and execute queries.

import psycopg2

class Postgres:
    def __init__(self, uri: str, database: str):
        """This class is used to connect to a Postgres database and execute queries.

        Args:
            uri (str): `postgresql://[user[:password]@][netloc][:port][/auth_dbname]`
            database (str): The name of the database to use for executing queries.
        """
        self.uri = uri
        self.database = database
        self.conn = None
        self.cursor = None
        
    def connect(self):
        """Connect to the PostgreSQL database."""
        try:
            self.conn = psycopg2.connect(self.uri + '/postgres')
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            
            # Check if the database exists, if not, create it
            self.cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.database}'")
            if not self.cursor.fetchone():
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                self.conn.commit()
                
            # Reconnect to the new database
            self.conn.close()
            self.conn = psycopg2.connect(f"{self.uri}/{self.database}")
            self.cursor = self.conn.cursor()
            
            # Enable the uuid-ossp extension
            self.cursor.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"")
            
            # Create the tables
            self.__setup_postgress_database_tables__()
            
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise
        
    def close(self):
        """Close the connection to the PostgreSQL database."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def __setup_postgress_database_tables__(self) -> None:
        """Setup the Postgres database tables."""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL
            )"""
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS files (
                id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
                user_id UUID NOT NULL REFERENCES users(id),
                file_path VARCHAR(255) NOT NULL,
                file_name VARCHAR(255) NOT NULL,
                file_type VARCHAR(50) NOT NULL,
                page_count INT NOT NULL
            )
            """
        )

    
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"Postgres(uri={self.uri}, database={self.database})"


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DATABASE"))
    postgress.connect()
    postgress.close()
    print("Postgres connection successful.")
