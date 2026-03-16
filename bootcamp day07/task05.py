import sqlite3
from task00 import load_json

def insert_laureates(json_file: str, db_name: str) -> None:
    data = load_json(json_file)
    laureates = data.get('laureates', [])

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for laureate in laureates:

        laureate_id = laureate.get('id')

        firstname = laureate.get('firstname', '')
        surname = laureate.get('surname', '')
        name = f"{firstname} {surname}".strip()
        gender = laureate.get('gender')
        born = laureate.get('born')
        died = laureate.get('died')

        born_country_id = laureate.get('bornCountryCode')
        died_country_id = laureate.get('diedCountryCode')

        cursor.execute('''
            INSERT OR IGNORE INTO laureates 
            (id, name, gender, born, died, born_country_id, died_country_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (laureate_id, name, gender, born, died, born_country_id, died_country_id))

    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM laureates")
    count = cursor.fetchone()[0]
    print(f"Inserted {count} laureates into database")
    
    conn.close()