from textblob import TextBlob

def get_sentiment(text: str) -> str:
    """
        This function analyzes the sentiment of text and return:
        POSITIVE, NEGETIVE or NUETRAL
    """

    blob = TextBlob(text=text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.1:
        return "positive"
    elif sentiment < -0.1:
        return "negative"
    else:
        return "neutral"