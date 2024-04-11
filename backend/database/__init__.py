# Path: backend/database/__init__.py
# Description: This file contains the code to connect to Postgres, MongoDB, and VectorDB databases.

import psycopg2
from pymongo import MongoClient
from pymilvus import Milvus, IndexType, MetricType
from .setup import setup_postgress_database_tables

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
            self.conn = psycopg2.connect(self.uri)
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.database}'")
            if not self.cursor.fetchone():
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                self.conn.commit()
            self.conn = psycopg2.connect(f"{self.uri}/{self.database}")
            setup_postgress_database_tables(self)
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise
        
    def execute_query(self, query):
        """Execute a query on the Postgres database.

        Args:
            query (str): The query to execute.
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            raise
        
    def close(self):
        """Close the connection to the PostgreSQL database."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"Postgres(uri={self.uri}, database={self.database})"

class MongoDB:
    def __init__(self, uri: str, database: str):
        """This class is used to connect to a MongoDB database and execute queries.

        Args:
            uri (str): MongoDB connection URI.
            database (str): The name of the database to use for executing queries.
        """
        self.uri = uri
        self.database = database
        self.client = None
        self.db = None
        
    def connect(self):
        """Connect to the MongoDB database."""
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database]
            self.db.create_collection("chunk_data")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise
        
    def close(self):
        """Close the connection to the MongoDB database."""
        if self.client:
            self.client.close()
        
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"MongoDB(uri={self.uri}, database={self.database})"

class VectorDB:
    def __init__(self, host: str, port: int, database_name: str):
        """
        This class is used to connect to a Milvus database and execute queries.

        Args:
            host (str): Milvus server host.
            port (int): Milvus server port.
            collection_name (str): The name of the collection to use for executing queries.
        """
        self.host = host
        self.port = port
        self.database_name = database_name
        self.collection_name = "embeddings"
        self.client = None
        self.collection = None

    def connect(self):
        """Connect to the Milvus database."""
        try:
            self.client = Milvus(host=self.host, port=self.port)
            
            # Check if `self.database_name` exists, if not create it
            if self.database_name not in self.client.list_databases():
                self.client.create_database(self.database_name)
            
            # Check if `self.collection_name` exists, if not create it
            if self.collection_name not in self.client.list_collections():
                collection_param = {
                    "collection_name": self.collection_name,
                    "database": self.database_name,
                    "fields": [
                        {"name": "id", "type": "VARCHAR", "index": True, "params": {"index_type": IndexType.IVF_FLAT, "metric_type": MetricType.L2, "params": {"nlist": 2048}}},
                        {"name": "embeddings", "type": "FLOAT_VECTOR", "params": {"dimension": 128}},
                    ],
                }
                self.client.create_collection(**collection_param)
                
                self.client.create_index(
                    collection_name=self.collection_name, 
                    index_type=IndexType.IVF_FLAT, 
                    params={"nlist": 2048}
                )
                
            self.collection = self.client.get_collection(self.collection_name)
        except Exception as e:
            print(f"Error connecting to Milvus: {e}")
            raise

    def close(self):
        """Close the connection to the Milvus database."""
        if self.client:
            self.client.close()

    def __del__(self):
        self.close()

    def __str__(self):
        return f"Milvus(host={self.host}, port={self.port}, database_name={self.database_name}, collection_name={self.collection_name})"

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv('..')
    
    # Connect to the Postgres database
    postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DATABASE"))
    postgress.connect()
    print(str(postgress))
    postgress.close()
    
    # Connect to the MongoDB database
    mongodb = MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE"))
    mongodb.connect()
    print(str(mongodb))
    mongodb.close()
    
    # Connect to the Milvus database
    vectordb = VectorDB(host=os.getenv("MILVUS_HOST"), port=os.getenv("MILVUS_PORT"), database_name=os.getenv("MILVUS_DATABASE"))
    vectordb.connect()
    print(str(vectordb))
    vectordb.close()
