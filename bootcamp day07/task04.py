import sqlite3
from task00 import load_json

def insert_countries(json_file, db_name: str) -> None:
    data= load_json(json_file)
    laureates= data.get('laureates', [])
    countries= set()
    for laureate in laureates:
        born_code= laureate.get('bornCountrycode')
        born_name= laureate.get('borncountry')
        if born_code and born_name:
            countries.add((born_code, born_name))

        died_code= laureate.get('diedCountryCode')
        died_name= laureate.get('diedCountry')
        if died_code and died_name:
            countries.add((died_code, died_name))
    conn= sqlite3.connect(db_name)
    cursor= conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries(
            code TEXT PRIMARY KEY,
            name TEXT NOT NULL
            )
    ''')
    for code, name in sorted(countries):
                cursor.execute(
                    "INSERT OR IGNORE INTO countries (code, name) VALUES (?,?)",
                    (code, name)
                )
    conn.commit()
    cursor.execute("SELECT COUNT (*) FROM  countries")
    count= cursor.fetchone()[0]
    print(f"Inserted {count} countries into database")
    conn.close()




