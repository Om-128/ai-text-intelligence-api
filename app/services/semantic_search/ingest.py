import os
import sys
import uuid
import warnings
warnings.filterwarnings("ignore")

from typing import Dict
from langchain_community.vectorstores import Chroma

from app.utils import CHROMA_DB_PATH
from app.CustomeException import CustomException
from app.services.semantic_search.embeddings import get_embedding_model

''' INGESTION '''
def ingest_text(text: str) -> Dict:
    """
        This function takes input from user and add it to Chroma DB
    """

    try:
        if not text or not text.strip():
            raise ValueError("Text must be a non-empty string")

        # Generate unique document ID
        doc_id = str(uuid.uuid4())
    
        ''' Intialize Chroma '''
        vector_store = Chroma(
            collection_name="text_intelligence",
            persist_directory=CHROMA_DB_PATH,
            embedding_function=get_embedding_model()
        )

        ''' Save to vectorstore '''
        vector_store.add_texts(
            texts=[text],
            ids=[doc_id]
        )

        return {
            "status": "success",
            "document_id": doc_id,
            "message": "Text ingested successfully"
        }

    except Exception as e:
        raise CustomException(e, sys)
