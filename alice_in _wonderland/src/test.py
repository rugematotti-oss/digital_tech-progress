import urllib.request
from src.tokenizer import tokenize_words, tokenize_sentences
from src.normalize import normalize
from src.lexdiv import compute_lexdiv
from src.entities import extract_entities

def fetch_book(book_id: int) -> str:
    "we're going to doanload the books from the Project Gutenberg website."
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    try:
        print(f"\nDownloading book {book_id}...")
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"sorry we couldn't download book {book_id}. Error: {e}")
        return ""


def analyse_book(book_id: int):
    "we're going to fectch the books using their IDs."
    text = fetch_book(book_id)
    if not text:
        return

    print("\nWhat would you like to do with this book?")
    print("  1 - Tokenize (words + sentences+ punctuation)")
    print("  2 - Tokenized + cleaned ")
    print("  3 - Lexical diversity metrics")
    print("  4 - Named entities (characters + locations)")
    print("  5 - Full analysis")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        words = tokenize_words(text)
        sentences = tokenize_sentences(text)
        print(f"\nWord tokens    : {len(words)}")
        print(f"Sentences      : {len(sentences)}")
        print(f"First 10 words : {words[:10]}")

    elif choice == "2":
        words = tokenize_words(text)
        clean = normalize(words, remove_stops=True)
        print(f"\nRaw tokens     : {len(words)}")
        print(f"Clean tokens   : {len(clean)}")
        print(f"First 10 clean : {clean[:10]}")

    elif choice == "3":
        print("\nComputing lexical diversity...")
        result = compute_lexdiv(text)
        print("\n=== Lexical Diversity ===")
        for key, value in result.items():
            print(f"  {key}: {value}")

    elif choice == "4":
        print("\nExtracting entities (this may take a moment)...")
        result = extract_entities(text)
        print("\n=== Characters ===")
        print(result["characters"])
        print("\n=== Locations ===")
        print(result["locations"])

    elif choice == "5":
        print("\nRunning full analysis (this may take a moment)...")

        words = tokenize_words(text)
        sentences = tokenize_sentences(text)
        clean = normalize(words, remove_stops=True)
        lexdiv = compute_lexdiv(text)
        entities = extract_entities(text)

        print(f"\n{'='*50}")
        print("FULL ANALYSIS REPORT")
        print(f"{'='*50}")

        print(f"\n--- Tokenization ---")
        print(f"  Word tokens : {len(words)}")
        print(f"  Sentences   : {len(sentences)}")
        print(f"  Clean tokens: {len(clean)}")

        print(f"\n--- Lexical Diversity ---")
        for key, value in lexdiv.items():
            print(f"  {key}: {value}")

        print(f"\n--- Characters ---")
        print(f"  {entities['characters']}")

        print(f"\n--- Locations ---")
        print(f"  {entities['locations']}")

    else:
        print("Invalid choice.")


# --- Main loop ---
print("="*50)
print("  Project Gutenberg Book Analyser")
print("="*50)
print("Reference IDs:")
print("  11  - Alice's Adventures in Wonderland")
print("  12  - Through the Looking-Glass")
print("  16  - Peter Pan")
print("  55  - The Wonderful Wizard of Oz")
print("  113 - The Secret Garden")
print("  120 - Treasure Island")
print("  236 - The Jungle Book")
print("  84  - Frankenstein")
print("  345 - Dracula")
print("  (or any other Gutenberg ID)")

while True:
    print("\n" + "-"*50)
    book_id = input("Enter a book ID (or 'quit' to exit): ").strip()

    if book_id.lower() == "quit":
        print("\nGoodbye!")
        break

    if not book_id.isdigit():
        print("Please enter a valid numeric ID.")
        continue

    analyse_book(int(book_id))