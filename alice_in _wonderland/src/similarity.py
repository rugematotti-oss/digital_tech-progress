from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocess import get_clean_text

BOOK_COLLECTION = {
    11: "Alice's Adventures in Wonderland",
    12: "Through the Looking-Glass",
    16: "Peter Pan",
    55: "The Wonderful Wizard of Oz",
    113: "The Secret Garden",
    120: "Treasure Island",
    236: "The Jungle Book",
    108: "The Return of Sherlock Holmes",
    834: "The Memoirs of Sherlock Holmes",
    863: "The Mysterious Affair at Styles",
    1661: "The Adventures of Sherlock Holmes",
    61262: "Poirot Investigates",
    69087: "The Murder of Roger Ackroyd",
    70114: "The Big Four",
    35: "The Time Machine",
    36: "The War of the Worlds",
    84: "Frankenstein; Or, The Modern Prometheus",
    159: "The Island of Doctor Moreau",
    164: "Twenty Thousand Leagues under the Sea",
    345: "Dracula",
}


def get_similarity_corpus() -> dict[int, str]:
    corpus = {}

    for corpus_id in BOOK_COLLECTION:
        try:
            corpus[corpus_id] = get_clean_text(corpus_id)
        except Exception:
            corpus[corpus_id] = ""

    return corpus


def get_similar_titles(book_id: int, top_k: int = 5, use_cache: bool = True) -> list[str]:
    try:
        target_text = get_clean_text(book_id)
    except Exception:
        return []

    if not target_text.strip():
        return []

    corpus = get_similarity_corpus()

    valid_ids = [bid for bid, text in corpus.items() if text.strip()]
    valid_texts = [corpus[bid] for bid in valid_ids]

    if len(valid_texts) < 2:
        return []

    all_ids = [book_id] + valid_ids
    all_texts = [target_text] + valid_texts

    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), min_df=2)
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix).flatten()

    scored_books = []
    for i in range(1, len(all_ids)):
        candidate_id = all_ids[i]
        score = similarities[i]
        scored_books.append((candidate_id, score))

    scored_books.sort(key=lambda x: x[1], reverse=True)

    top_books = scored_books[:top_k]

    return [BOOK_COLLECTION[candidate_id] for candidate_id, _ in top_books]