from fastapi import APIRouter, HTTPException, Body
from app.services.semantic_search.ingest import ingest_text

router = APIRouter()

@router.post("/add")
def add_text(text: str = Body(..., media_type="text/plain")):
    """
    Ingest user text into Chroma DB
    """
    try:
        return ingest_text(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))