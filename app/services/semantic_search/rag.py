import warnings
warnings.filterwarnings("ignore")

import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

import sys
from typing import Dict, List

from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

from app.utils import CHROMA_DB_PATH
from app.CustomeException import CustomException
from app.services.semantic_search.embeddings import embedding_model


''' LLM '''
llm = Ollama(
    model="gemma:2b",
    temperature=0.2
)

''' PROMPT '''
RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant.

You are given retrieved source text as context.
Answer the question by carefully checking the context.

Rules:
- If the answer is explicitly stated OR clearly implied in the context, answer the question.
- You may paraphrase the context when answering.
- Do NOT use outside knowledge.
- If the context is completely unrelated or insufficient, say:
  "I don't know based on the given sources."

Context:
{context}

Question:
{question}

Answer:
"""
)


''' RAG '''

def rag_query(query: str, top_k: int = 3) -> Dict:
    """
    Retrieve relevant context from Chroma DB and generate answer
    """
    try:
        if not query or not query.strip():
            raise ValueError("Query must be a non-empty string")

        ''' Load vector store '''
        vector_store = Chroma(
            collection_name="text_intelligence",
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embedding_model
        )

        docs = vector_store.similarity_search(query, k=top_k)

        if not docs:
            return {"answer": "I don't know", "sources": []}

        context = "\n\n".join(d.page_content for d in docs)

        answer = llm.invoke(
            RAG_PROMPT.format(
                context=context,
                question=query
            )
        )

        return {
            "answer": answer,
            "sources": [d.page_content for d in docs]
        }

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    result = rag_query("who created AI?")
    print(result)


