from fastapi import APIRouter
from pydantic import BaseModel
from app.services.sentiment_service import get_sentiment
from app.services.keyword_service import get_top_words

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    sentiment: str
    keywords: list[str]

@router.post("/", response_model=AnalyzeResponse)
def analyze_text(request: AnalyzeRequest):
    sentiment = get_sentiment(request.text)
    keywords = get_top_words(request.text)
    return {
        "sentiment": sentiment,
        "keywords": keywords
    }
