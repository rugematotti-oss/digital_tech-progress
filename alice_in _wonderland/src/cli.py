import argparse
import json

from src.card import build_card
from src.topics import extract_topics
from src.entities import extract_entities
from src.summarize import summarize_book
from src.similarity import get_similar_titles
from bonus.author.author_books import find_books_by_author, download_books


def parse_args():
    parser = argparse.ArgumentParser(
        description="Bookworm - lightweight NLP CLI for Project Gutenberg books"
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--topics", type=int, metavar="ID", help="Extract topics for a book")
    group.add_argument("--entities", type=int, metavar="ID", help="Extract entities for a book")
    group.add_argument("--summarize", type=int, metavar="ID", help="Summarize a book")
    group.add_argument("--similar", type=int, metavar="ID", help="Find similar books")
    group.add_argument("--card", type=int, metavar="ID", help="Generate a full book card")
    group.add_argument("--lexdiv", type=int, metavar="ID", help="Compute lexical diversity")
    group.add_argument("--author", type=str, metavar="NAME", help="Retrieve books by author")

    parser.add_argument("--download", action="store_true", help="Download matching author books")

    return parser.parse_args()


def run_cli():
    args = parse_args()

    if args.topics is not None:
        result = extract_topics(args.topics)
    elif args.entities is not None:
        result = extract_entities(args.entities)
    elif args.summarize is not None:
        result = summarize_book(args.summarize)
    elif args.similar is not None:
        result = get_similar_titles(args.similar)
    elif args.card is not None:
        result = build_card(args.card)
    elif args.lexdiv is not None:
        from src.loader import load_book_text
        from src.lexdiv import compute_lexdiv

        text = load_book_text(args.lexdiv)
        result = compute_lexdiv(text)
    elif args.author is not None:
        books = find_books_by_author(args.author)

        result = {
            "author": args.author,
            "count": len(books),
            "books": books
        }

        if args.download:
            result["downloads"] = download_books(books)
    else:
        raise ValueError("No valid command provided.")

    if isinstance(result, str):
        print(result)
    else:
        print(json.dumps(result, indent=4, ensure_ascii=False))


def main():
    run_cli()