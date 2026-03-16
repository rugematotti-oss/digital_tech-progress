import sqlite3
from task00 import load_json

def insert_categories(json_file: str, db_name: str) -> None:

    data = load_json(json_file)
    laureates = data.get('laureates', [])
    
    categories = set()
    for laureate in laureates:
        prizes = laureate.get('prizes', [])
        for prize in prizes:
            category = prize.get('category')
            if category:
                categories.add(category)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for category in sorted(categories):
        try:
            cursor.execute(
                "INSERT INTO categories (name) VALUES (?)",
                (category,)
            )
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()
    
    print(f"Categories inserted successfully")