import sqlite3
from task00 import load_json

def insert_prizes(json_file: str, db_name: str) -> None:

    data = load_json(json_file)
    laureates = data.get('laureates', [])
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    prizes_count = 0
    for laureate in laureates:
        laureate_id = laureate.get('id')
        prizes = laureate.get('prizes', [])
        
        for prize in prizes:
            year = prize.get('year')
            category_name = prize.get('category')
            cursor.execute(
                "SELECT id FROM categories WHERE name = ?",
                (category_name,)
            )
            category_result = cursor.fetchone()
            
            if not category_result:
                continue  
            
            category_id = category_result[0]

            affiliation_country_id = None
            affiliations = prize.get('affiliations', [])
            
            if affiliations and len(affiliations) > 0:
                affiliation = affiliations[0]
                if isinstance(affiliation, dict):
                    country = affiliation.get('country')
                    if isinstance(country, dict):
                        affiliation_country_id = country.get('code')
                    elif isinstance(country, str):
                        affiliation_country_id = country
            cursor.execute('''
                INSERT INTO prizes 
                (laureate_id, category_id, year, affiliation_country_id)
                VALUES (?, ?, ?, ?)
            ''', (laureate_id, category_id, year, affiliation_country_id))
            
            prizes_count += 1
    conn.commit()
    
    print(f"Inserted {prizes_count} prizes into database")
    
    conn.close()