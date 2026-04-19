from collections import Counter

from src.preprocess import get_clean_text
from src.tokenize import tokenize_words
from src.normalize import normalize

EXTRA_STOPWORDS = {
    "said", "one", "like", "would", "could", "know",
    "went", "im", "dont", "thats", "youre"
}


def split_into_sections(text: str, n_sections: int = 4) -> dict[int, str]:
    length = len(text)
    section_size = length // n_sections

    sections = {}
    for i in range(n_sections):
        start = i * section_size
        end = (i + 1) * section_size if i < n_sections - 1 else length
        sections[i + 1] = text[start:end]

    return sections


def extract_top_words(text: str, top_n: int = 10) -> list[str]:
    tokens = tokenize_words(text)
    tokens = normalize(tokens)

    tokens = [
        token for token in tokens
        if len(token) > 2 and token not in EXTRA_STOPWORDS
    ]

    freq = Counter(tokens)
    return [word for word, _ in freq.most_common(top_n)]


def extract_topics(
    book_id: int,
    n_sections: int = 4,
    top_n: int = 10,
    use_cache: bool = True
) -> dict:
    text = get_clean_text(book_id)

    if not text.strip():
        return {i: [] for i in range(1, n_sections + 1)}

    sections = split_into_sections(text, n_sections)

    topics = {}
    for section_id, section_text in sections.items():
        topics[section_id] = extract_top_words(section_text, top_n)

    return topics