from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import os

''' Paths '''
BASE_DIR = BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)

CHROMA_DB_PATH = os.path.join(BASE_DIR, "vectorstore", "chroma_db")

''' Embedding Model '''
Embedding_Model = "sentence-transformers/all-MiniLM-L6-v2"

embedding_function = HuggingFaceBgeEmbeddings(
    model = Embedding_Model
)

''' Vector store '''
vector_store = Chroma(
    persist_directory = CHROMA_DB_PATH. 
    embedding_function = embedding_function
)