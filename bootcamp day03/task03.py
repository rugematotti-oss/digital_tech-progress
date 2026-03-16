
def display_categories(db):
    prizes = db["prizes"]
    categories = set()

    for p in prizes.find({}, {"category": 1, "_id": 0}):
        if "category" in p:
            categories.add(p["category"])

    result = sorted(categories, key=lambda x: x.lower())
    print(result)
    return result


def display_laureates(db):
    laureates_col = db["laureates"]
    names = []

    for l in laureates_col.find({}, {"firstname": 1, "surname": 1, "_id": 0}):
        firstname = l.get("firstname", "").strip()
        surname = l.get("surname", "").strip()

        if surname:
            fullname = f"{firstname} {surname}"
        else:
            fullname = firstname

        if fullname:
            names.append(fullname)

    result = sorted(names, key=lambda x: x.lower())
    print(result)
    return result


def display_countries(db):
    countries_col = db["countries"]
    countries = []

    for c in countries_col.find({}, {"name": 1, "code": 1, "_id": 0}):
        name = c.get("name", "").strip()
        code = c.get("code", "").strip()
        if name:
            countries.append((name, code))

    result = sorted(countries, key=lambda x: x[0].lower())
    print(result)
    return result
    
