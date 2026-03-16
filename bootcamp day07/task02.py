import sqlite3
def create_database(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS laureates (
            id INTEGER PRIMARY KEY,
            firstname TEXT NOT NULL,
            surname TEXT,
            born_country_code TEXT,
            born_country TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prizes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            laureate_id INTEGER NOT NULL,
            motivation TEXT,
            share INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id),
            FOREIGN KEY (laureate_id) REFERENCES laureates(id)
        )
    ''')
    conn.commit()
    conn.close()
    
    print(f"Database created successfully at: {db_path}") 

