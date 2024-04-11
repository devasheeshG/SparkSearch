from backend.database.postgres import Postgres
from mongodb import MongoDB
from milvus import VectorDB
import os
from dotenv import load_dotenv
from colorama import Fore
from tabulate import tabulate

def print_connection_status(status):
    symbol = "✓" if status else "✗"
    color = Fore.GREEN if status else Fore.RED
    return f"{color}{symbol}{Fore.RESET}"

if __name__ == "__main__":
    load_dotenv('../.env')

    data = []

    # Connect to the Postgres database
    try:
        postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DATABASE"))
        postgress.connect()
        data.append(["Postgres", print_connection_status(True), str(postgress)])
    except Exception as e:
        data.append(["Postgres", print_connection_status(False), str(e)])
    finally:
        postgress.close()

    # Connect to the MongoDB database
    try:
        mongodb = MongoDB(uri=os.getenv("MONGODB_URI"), database=os.getenv("MONGODB_DATABASE"))
        mongodb.connect()
        data.append(["MongoDB", print_connection_status(True), str(mongodb)])
    except Exception as e:
        data.append(["MongoDB", print_connection_status(False), str(e)])
    finally:
        mongodb.close()

    # Connect to the Milvus database
    try:
        vectordb = VectorDB(uri=os.getenv("MILVUS_URI"), database_name=os.getenv("MILVUS_DATABASE"))
        vectordb.connect()
        data.append(["Milvus", print_connection_status(True), str(vectordb)])
    except Exception as e:
        data.append(["Milvus", print_connection_status(False), str(e)])
    finally:
        vectordb.close()

    headers = ["Database", "Status", "Message"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
