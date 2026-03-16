import json

def load_json(filepath: str) -> dict:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content[:100])
    data = json.loads(content)
    
    return data


