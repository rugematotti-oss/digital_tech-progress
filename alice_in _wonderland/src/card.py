from src.preprocess import get_clean_text
from src.lexdiv import compute_lexdiv
from src.topics import extract_topics
from src.entities import extract_entities
from src.summarize import summarize_book
from src.similarity import get_similar_titles
from src.loader import get_book_info


def build_card(book_id: int, use_cache: bool = True) -> dict:
    clean_text = get_clean_text(book_id)

    return {
        "info": get_book_info(book_id),
        "lexdiv": compute_lexdiv(clean_text),
        "topics": extract_topics(book_id, use_cache=use_cache),
        "entities": extract_entities(book_id, use_cache=use_cache),
        "summary": summarize_book(book_id, use_cache=use_cache),
        "similar": get_similar_titles(book_id, use_cache=use_cache),
    }