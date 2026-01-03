from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
import time

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
PC_API_KEY = os.getenv("PINECONE_API_KEY")


# ... your other imports


def embed_and_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    index_name = "interview-ai-app"

    # 1. Initialize the vector store without documents first
    vectorstore = PineconeVectorStore(
        index_name=index_name, embedding=embeddings, pinecone_api_key=PC_API_KEY
    )

    # 2. Add documents in small batches to avoid 429 errors
    batch_size = 5
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        vectorstore.add_documents(batch)
        time.sleep(2)  # Pause for 2 seconds between batches

    return vectorstore
