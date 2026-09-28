import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient , models
from qdrant_client.models import Distance, VectorParams

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")



qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=300,
)

COLLECTION_NAME = "ritik"

def create_collection():

    collections = qdrant_client.get_collection()

    exists = any(
        collection.name == COLLECTION_NAME
        for collection in collections.collections
    )

    if not exists:

        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size = 384,
                distance=Distance.COSINE
            )

        )
        print(
            f"Created Qdrant collection: {COLLECTION_NAME}"
        )
    else:
        print(
            f"Qdrant collection already exists:",
            f"{COLLECTION_NAME}"
        )

    
