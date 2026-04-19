import os
import re
import requests
import pandas as pd
from src.config import BOOKS_PATH, CATALOG_PATH

def download_book(book_id):
    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    path = f"{BOOKS_PATH}{book_id}.txt"

    # si le dossier n'existe pas (je le crée)
    os.makedirs(BOOKS_PATH, exist_ok=True)

    response = requests.get(url)

    if response.status_code == 200:
        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        raise Exception(f"Erreur téléchargement livre {book_id}")

def load_book_text(book_id):
    path = f"{BOOKS_PATH}{book_id}.txt"

    # si le fichier n'existe pas (je télécharge)
    if not os.path.exists(path):
        download_book(book_id)

    # lire le fichier
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_metadata_field(text: str, field_name: str) -> str:
    pattern = rf"^\s*{field_name}\s*:\s*(.+)$"
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else ""

def extract_title_and_author_from_header(text: str) -> tuple[str, str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    title = ""
    author = ""

    for i, line in enumerate(lines):
        if "project gutenberg ebook" in line.lower():
            for j in range(i + 1, min(i + 15, len(lines))):
                current = lines[j]

                if current.startswith("[") and current.endswith("]"):
                    continue
                if current.isupper() and len(current.split()) > 4:
                    continue
                if current.lower().startswith("contents"):
                    continue

                if not title:
                    title = current
                    continue

                if current.lower().startswith("by "):
                    author = current[3:].strip()
                    break

    return title, author

def get_book_info(book_id) -> dict:
    try:
        df = pd.read_csv(CATALOG_PATH)
        row = df[df["Text#"] == int(book_id)]

        if not row.empty:
            row = row.iloc[0]

            title = str(row["Title"]).strip() if pd.notna(row["Title"]) else ""
            authors = str(row["Authors"]).strip() if pd.notna(row["Authors"]) else ""
            bookshelves = str(row["Bookshelves"]).strip() if pd.notna(row["Bookshelves"]) else ""

            return {
                "id": str(book_id),
                "title": title if title else "Unknown title",
                "authors": authors if authors else "Unknown author",
                "bookshelves": bookshelves if bookshelves else "Unknown bookshelf",
            }
    except Exception:
        pass

    # fallback si le CSV ne marche pas
    text = load_book_text(book_id)

    # on ne prend que le début du fichier (header Gutenberg)
    header = text[:15000]

    title = extract_metadata_field(header, "Title")
    author = extract_metadata_field(header, "Author")

    # fallback si pas de champs "Title:" / "Author:"
    if not title or not author:
        fallback_title, fallback_author = extract_title_and_author_from_header(header)
        if not title:
            title = fallback_title
        if not author:
            author = fallback_author

    return {
        "id": str(book_id),
        "title": title if title else "Unknown title",
        "authors": author if author else "Unknown author",
        "bookshelves": "Unknown bookshelf",
    }