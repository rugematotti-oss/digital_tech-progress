import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


def tokenize_words(text: str) -> list[str]:
    return word_tokenize(text)


def tokenize_sentences(text: str) -> list[str]:
    return sent_tokenize(text)