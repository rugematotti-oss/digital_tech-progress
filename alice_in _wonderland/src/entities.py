import re
from collections import Counter

from src.loader import load_book_text

BLOCKLIST = {
    "The", "And", "You", "But", "For", "Not", "This", "That",
    "Then", "There", "What", "Why", "How", "Yes", "No",
    "Ive", "Im", "Ill", "Oh", "Well", "If", "So", "Now"
}

LOCATION_WORDS = {
    "Wonderland", "England", "London", "Paris", "Court", "Garden", "House",
    "Jerusalem", "Egypt", "Israel", "Judah", "Bethlehem", "Nazareth",
    "Galilee", "Babylon", "Samaria", "Zion", "Canaan", "Eden"
}


def extract_entities(book_id: int, use_cache: bool = True) -> dict:
    text = load_book_text(book_id)

    words = re.findall(r"\b[A-Z][a-z]+\b", text)
    words = [w for w in words if len(w) > 2 and w not in BLOCKLIST]

    freq = Counter(words)
    common = [word for word, _ in freq.most_common(80)]

    characters = []
    locations = []

    for word in common:
        if word in LOCATION_WORDS:
            locations.append(word)
        else:
            characters.append(word)

    return {
        "characters": characters[:10],
        "locations": locations[:10],
    }