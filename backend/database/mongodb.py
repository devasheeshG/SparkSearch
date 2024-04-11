# Path: backend/database/mongodb.py
# Description: This file contains the code to connect to a MongoDB database and execute queries.

from pymongo import MongoClient

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
            if "chunk_data" not in self.db.list_collection_names():
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
