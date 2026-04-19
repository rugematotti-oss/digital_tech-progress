import os
import sys
import json
import argparse
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.config import CATALOG_PATH
from src.loader import download_book


def find_books_by_author(author_name: str) -> list[dict]:
    df = pd.read_csv(CATALOG_PATH)

    # garder les lignes où Authors existe
    df = df[df["Authors"].notna()]

    # filtrage insensible à la casse
    filtered = df[df["Authors"].str.contains(author_name, case=False, na=False)]

    books = []
    for _, row in filtered.iterrows():
        books.append({
            "id": int(row["Text#"]) if pd.notna(row["Text#"]) else None,
            "title": str(row["Title"]).strip() if pd.notna(row["Title"]) else "Unknown title",
            "authors": str(row["Authors"]).strip() if pd.notna(row["Authors"]) else "Unknown author",
            "bookshelves": str(row["Bookshelves"]).strip() if pd.notna(row["Bookshelves"]) else "Unknown bookshelf",
        })

    return books


def download_books(books: list[dict]) -> list[dict]:
    downloaded = []

    for book in books:
        book_id = book["id"]
        if book_id is None:
            continue

        try:
            download_book(book_id)
            downloaded.append({
                "id": book_id,
                "title": book["title"],
                "status": "downloaded"
            })
        except Exception as e:
            downloaded.append({
                "id": book_id,
                "title": book["title"],
                "status": f"failed: {e}"
            })

    return downloaded


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve and optionally download all books written by a given author."
    )
    parser.add_argument("author", type=str, help="Author name to search")
    parser.add_argument("--download", action="store_true", help="Download all matching books")

    args = parser.parse_args()

    books = find_books_by_author(args.author)

    if not books:
        print(json.dumps({"author": args.author, "books": []}, indent=4, ensure_ascii=False))
        return

    result = {
        "author": args.author,
        "count": len(books),
        "books": books
    }

    if args.download:
        result["downloads"] = download_books(books)

    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()