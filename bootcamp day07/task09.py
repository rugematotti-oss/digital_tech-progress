import sqlite3

def peace_prizes(db_name: str) -> list[tuple[int, str]]:

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = """
        SELECT p.year, p.motivation
        FROM prizes p
        JOIN categories c ON p.category_id = c.id
        WHERE c.name = 'peace'
          AND p.motivation IS NOT NULL
        GROUP BY p.year, p.motivation
        HAVING COUNT(p.laureate_id) = 2
        ORDER BY p.year
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    
    return results
