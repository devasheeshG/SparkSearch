# Path: backend/database/__init__.py

import psycopg2
from pymongo import MongoClient

class Postgres:
    def __init__(self, uri: str, database: str):
        """This class is used to connect to a Postgres database and execute queries.

        Args:
            uri (str): `postgresql://[user[:password]@][netloc][:port][/auth_dbname]`
            database (str): The name of the database to use for executing queries.
        """
        self.uri = uri
        self.database = database
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Connect to the Postgres database."""
        self.connection = psycopg2.connect(self.uri)
        self.cursor = self.connection.cursor()
        
    def execute(self, query):
        """Execute a query on the Postgres database.

        Args:
            query (str): The query to execute.
        """
        self.cursor.execute(query)
        self.connection.commit()
        
    def close(self):
        """Close the connection to the Postgres database."""
        self.cursor.close()
        self.connection.close()
        
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"Postgres(uri={self.uri}, database={self.database})"
    
    def __repr__(self):
        return str(self)

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
        self.client = MongoClient(self.uri)
        self.db = self.client[self.database]
        
    def close(self):
        """Close the connection to the MongoDB database."""
        self.client.close()
        
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"MongoDB(uri={self.uri}, database={self.database})"
    
    def __repr__(self):
        return str(self)
    
def test_postgres():
    try:
        import os
        uri = os.getenv("POSTGRES_URI")
        database = os.getenv("POSTGRES_DATABASE")
        
        with Postgres(uri, database) as db:
            db.execute("SELECT version();")
            db_version = db.cursor.fetchone()
            print("Connected to PostgreSQL database version:", db_version[0])
            
    except Exception as e:
        print("Error connecting to PostgreSQL database:", e)

def test_mongodb():
    try:
        import os
        uri = os.getenv("MONGODB_URI")
        database = os.getenv("MONGODB_DATABASE")
        
        with MongoDB(uri, database) as db:
            test_db = db.client.get_database()
            test_collection = test_db.get_collection('test_collection')
            
            # Insert a test document
            test_document = {'test_key': 'test_value'}
            test_collection.insert_one(test_document)
            
            # Query the inserted document
            result = test_collection.find_one({'test_key': 'test_value'})
            if result:
                print("Connected to MongoDB successfully.")
            else:
                print("Failed to connect to MongoDB.")
                
    except Exception as e:
        print("Error connecting to MongoDB database:", e)
                  
if __name__ == "__main__":
    from dotenv import load_dotenv
    import sys
    sys.path.append("../")
    load_dotenv()
    
    test_postgres()
    test_mongodb()
