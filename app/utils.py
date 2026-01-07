import os

''' PATHS '''
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

CHROMA_DB_PATH = os.path.join(BASE_DIR, "vectorstore", "chroma_db")