from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.api.summarize import router as summarize_router

app = FastAPI(
    title="AI Text Intelligence API",
    description="NLP-powered API for sentiment analysis",
    version="1.0.0",
)

app.include_router(
    analyze_router,
    prefix="/analyze",
    tags=["analyze"]
)

app.include_router(
    summarize_router,
    prefix="/summarize",
    tags=["summarize"]
)