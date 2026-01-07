import warnings
warnings.filterwarnings("ignore")

import os
import sys
from langchain_community.embeddings import HuggingFaceEmbeddings

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME
)

def get_embedding_model() -> HuggingFaceEmbeddings:
    return embedding_model