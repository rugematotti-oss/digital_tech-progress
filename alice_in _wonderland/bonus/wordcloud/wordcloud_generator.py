import os
import sys
from collections import Counter

from wordcloud import WordCloud
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.preprocess import get_clean_text
from src.tokenize import tokenize_words
from src.normalize import normalize


EXTRA_STOPWORDS = {
    "said", "one", "like", "would", "could", "know",
    "went", "im", "dont", "thats", "youre"
}


def get_frequencies(book_id: int) -> dict[str, int]:
    text = get_clean_text(book_id)
    tokens = tokenize_words(text)
    tokens = normalize(tokens)

    tokens = [
        token for token in tokens
        if len(token) > 2 and token not in EXTRA_STOPWORDS
    ]

    return dict(Counter(tokens))


def generate_wordcloud(book_id: int) -> str:
    frequencies = get_frequencies(book_id)

    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{book_id}_wordcloud.png")

    wc = WordCloud(width=1200, height=600, background_color="white")
    wc.generate_from_frequencies(frequencies)
    wc.to_file(output_path)

    return output_path


def main():
    if len(sys.argv) != 2:
        print("Usage: python wordcloud_generator.py <book_id>")
        sys.exit(1)

    try:
        book_id = int(sys.argv[1])
    except ValueError:
        print("Book ID must be an integer.")
        sys.exit(1)

    output_path = generate_wordcloud(book_id)
    print(f"Word cloud generated: {output_path}")


if __name__ == "__main__":
    main()