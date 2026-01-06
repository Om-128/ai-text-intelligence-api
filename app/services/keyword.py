from sklearn.feature_extraction.text import TfidfVectorizer

def get_top_words(text : str, top_k: int = 5) -> list[str]:
    """
        This function takes text input and returns top k words
    """

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=top_k
    )

    vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out()

    return keywords
