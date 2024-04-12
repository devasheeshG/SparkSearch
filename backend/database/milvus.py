# Path: backend/database/milvus.py
# Description: This file contains the code to connect to a Milvus database and execute queries.

from pymilvus import MilvusClient, IndexType, db, DataType, connections

class VectorDB:
    def __init__(self, uri: str, database_name: str):
        """
        This class is used to connect to a Milvus database and execute queries.

        Args:
            uri (str): Milvus connection URI.
            collection_name (str): The name of the collection to use for executing queries.
        """
        self.uri = uri
        self.database_name = database_name
        self.collection_name = "embeddings"
        self.client = None

    def connect(self):
        """
        Connect to the Milvus database.
        
        This method establishes a connection to the Milvus database server, creates the specified database if it doesn't exist,
        and creates the specified collection if it doesn't exist.
        """
        try:
            # Establish connection to Milvus server
            self.client = MilvusClient(uri=self.uri, timeout=10)
            connections.connect(host=self.uri.split("://")[1].split(':')[0], port=self.uri.split(":")[2].split("/")[0])
            # Check if the specified database exists, if not create it
            if self.database_name not in db.list_database():
                db.create_database(self.database_name)
            db.using_database(self.database_name)
            
            # Check if the specified collection exists, if not create it
            if self.collection_name not in self.client.list_collections():
                # Define collection schemas
                schema = MilvusClient.create_schema(
                    auto_id=False,
                    enable_dynamic_field=True,
                )
                schema.add_field(field_name="id", datatype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=36)
                schema.add_field(field_name="embeddings", datatype=DataType.FLOAT_VECTOR, dim=128)
                
                # Define index parms
                index_parms = self.client.prepare_index_params()
                index_parms.add_index(
                    field_name="embeddings",
                    index_type=IndexType.IVF_FLAT,
                    metric_type="L2",
                    params={"nlist": 2048}
                )
                
                # Create the collection
                self.client.create_collection(collection_name=self.collection_name, schema=schema, index_params=index_parms)
                
                # Load collection
                while not self.client.get_load_state(self.collection_name)["state"] == "<LoadState: Loaded>":
                    self.client.load_collection(self.collection_name)

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
        return f"Milvus(uri={self.uri}, database_name={self.database_name})"

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    try:
        vectordb = VectorDB(uri=os.getenv("MILVUS_URI"), database_name=os.getenv("MILVUS_DATABASE"))
        vectordb.connect()
    except Exception as e:
        print(f"Error connecting to Milvus: {e}")
        import traceback
        traceback.print_exc()  # Print the traceback for debugging purposes
    finally:
        if vectordb:
            vectordb.close()
    