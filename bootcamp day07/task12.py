from sqlalchemy import and_
from task11 import init_sqla, Laureate, Prize, Category
import re


def scrabble(session) -> list[str]:


    consonants = 'bcdfghjklmnpqrstvwxyz'
    results = session.query(Prize.motivation, Laureate.name)\
        .join(Laureate, Prize.laureate_id == Laureate.id)\
        .join(Category, Prize.category_id == Category.id)\
        .filter(Category.name == 'peace')\
        .filter(Prize.motivation.isnot(None))\
        .all()
    
    motivations = set()
    
    for motivation, name in results:
        name_lower = name.lower()
        has_double_consonant = False
        for i in range(len(name_lower) - 1):
            char1 = name_lower[i]
            char2 = name_lower[i + 1]
            if char1 == char2 and char1 in consonants:
                has_double_consonant = True
                break
        
        if has_double_consonant:
            motivations.add(motivation)

    return sorted(list(motivations))
if __name__ == "__main__":
    session = init_sqla("nobel.db")
    
    result = scrabble(session)
    print(f"Found {len(result)} unique motivations")
    print("\nMotivations:")
    for motivation in result:
        print(f"  - {motivation}")
    
    session.close()