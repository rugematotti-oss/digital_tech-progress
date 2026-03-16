import sqlite3

def prizes_by_category(db_name: str) -> list[list[int]]:
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT c.code
        FROM countries c
        JOIN laureates l ON c.code = l.born_country_id
        ORDER BY c.code
    """)
    countries = [row[0] for row in cursor.fetchall()]
    cursor.execute("""
        SELECT id, name
        FROM categories
        ORDER BY name
    """)
    categories = cursor.fetchall()
    category_ids = [cat[0] for cat in categories]
    matrix = []
    
    for country_code in countries:
        row = []
        for category_id in category_ids:

            cursor.execute("""
                SELECT COUNT(*)
                FROM prizes p
                JOIN laureates l ON p.laureate_id = l.id
                WHERE l.born_country_id = ?
                  AND p.category_id = ?
            """, (country_code, category_id))
            
            count = cursor.fetchone()[0]
            row.append(count)
        
        matrix.append(row)
    
    conn.close()
    
    return matrix
