import re
from collections import Counter

from src.loader import load_book_text
from src.tokenize import tokenize_words, tokenize_sentences
from src.normalize import normalize

EXTRA_STOPWORDS = {
    "said", "one", "like", "would", "could", "know",
    "went", "im", "dont", "thats", "youre"
}


def clean_sentence(sentence: str) -> str:
    sentence = sentence.replace("\n", " ")
    sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence


def get_word_frequencies(text: str) -> dict[str, int]:
    tokens = tokenize_words(text)
    tokens = normalize(tokens)

    tokens = [
        token for token in tokens
        if len(token) > 2 and token not in EXTRA_STOPWORDS
    ]

    return dict(Counter(tokens))


def is_valid_summary_sentence(sentence: str) -> bool:
    sentence = clean_sentence(sentence)

    if not sentence:
        return False

    word_count = len(sentence.split())

    if word_count < 8:
        return False
    if word_count > 35:
        return False
    if sentence.upper().startswith("CHAPTER"):
        return False
    if "project gutenberg" in sentence.lower():
        return False
    if sentence.count('"') >= 2:
        return False

    return True


def score_sentence(sentence: str, word_freq: dict[str, int]) -> float:
    tokens = tokenize_words(sentence)
    tokens = normalize(tokens)

    if not tokens:
        return 0.0

    score = sum(word_freq.get(token, 0) for token in tokens)
    return score / len(tokens)


def summarize_book(book_id: int, max_sentences: int = 3, use_cache: bool = True) -> str:
    text = load_book_text(book_id)
    sentences = tokenize_sentences(text)

    if not sentences:
        return ""

    word_freq = get_word_frequencies(text)

    scored_sentences = []
    for index, sentence in enumerate(sentences):
        cleaned = clean_sentence(sentence)

        if not is_valid_summary_sentence(cleaned):
            continue

        score = score_sentence(cleaned, word_freq)
        scored_sentences.append((index, cleaned, score))

    if not scored_sentences:
        fallback = [clean_sentence(s) for s in sentences[:max_sentences]]
        return " ".join(fallback).strip()

    best_sentences = sorted(scored_sentences, key=lambda x: x[2], reverse=True)[:max_sentences]
    best_sentences = sorted(best_sentences, key=lambda x: x[0])

    return " ".join(sentence for _, sentence, _ in best_sentences)

