import torch
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-base")

def get_summary(text: str) -> str:
    """
        This function takes text input as uses BART to summarize it
        and returns the summary
    """
    cleaned_text = text.replace("\r", " ").replace("\n", " ")
    summary = summarizer(cleaned_text, max_length=150, min_length=30, do_sample=False)
    return summary[0]["summary_text"]