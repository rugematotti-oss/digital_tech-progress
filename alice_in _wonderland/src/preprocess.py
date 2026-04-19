import re
from src.loader import load_book_text

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def get_clean_text(book_id):
    text = load_book_text(book_id)
    return clean_text(text)