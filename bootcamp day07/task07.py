import sqlite3

def multiple_prizes(db_name: str) -> list[str]:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = """
        SELECT l.name, COUNT(p.id) as prize_count
        FROM laureates l
        JOIN prizes p ON l.id = p.laureate_id
        GROUP BY l.id, l.name
        HAVING COUNT(p.id) > 1
        ORDER BY l.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()

    names = [row[0] for row in results]
    
    conn.close()
    
    return names
