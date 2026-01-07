from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.api.summarize import router as summarize_router
from app.api.semantic_add import router as semantic_add_router
from app.api.semantic_search import router as semantic_search_router

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

app.include_router(
    semantic_add_router,
    prefix="/semantic_add",
    tags=["semantic_add"]
)

app.include_router(
    semantic_search_router,
    prefix="/semantic_search",
    tags=["semantic_search"]
)