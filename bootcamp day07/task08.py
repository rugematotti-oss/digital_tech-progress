import sqlite3

def french_prizes(db_name: str) -> list[str]:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = """
        SELECT name
        FROM laureates
        WHERE born_country_id = 'FR'
        ORDER BY name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    names = [row[0] for row in results]
    
    conn.close()
    
    return names


