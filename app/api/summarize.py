from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.services.summarization_service import get_summary

router = APIRouter()

""" For input instead of using BaseModel we used plain text """

class AnalyzeResponse(BaseModel):
    summary: str

@router.post("/", response_model=AnalyzeResponse)
def summarize_text(text: str = Body(..., media_type="text/plain")):
    summary = get_summary(text)
    return {"summary": summary}