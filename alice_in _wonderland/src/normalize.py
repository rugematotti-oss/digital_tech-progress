
import string
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

STOPWORDS = set(stopwords.words("english"))


def to_lowercase(tokens: list[str]) -> list[str]:
    return [token.lower() for token in tokens]


def remove_punctuation(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in string.punctuation]


def remove_stopwords(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOPWORDS]


def normalize(tokens: list[str], remove_stops: bool = True) -> list[str]:
    tokens = to_lowercase(tokens)
    tokens = remove_punctuation(tokens)
    if remove_stops:
        tokens = remove_stopwords(tokens)
    return tokens
