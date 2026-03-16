from task00 import load_json

def display_info() -> None:
    data = load_json("./nobels.json")
    laureates = data.get('laureates', [])
    categories = set()
    for laureate in laureates:
        prizes = laureate.get('prizes', [])
        for prize in prizes:
            category = prize.get('category')
            if category:
                categories.add(category)
    categories_sorted = sorted(list(categories))

    full_names = []
    for laureate in laureates:
        firstname = laureate.get('firstname', '')
        surname = laureate.get('surname', '')
        if firstname and surname:
            full_name = f"{firstname} {surname}"
            full_names.append(full_name)
        elif firstname:
            full_names.append(firstname)

    full_names_sorted = sorted(full_names)

    birth_countries = set()
    for laureate in laureates:
        born_country_code = laureate.get('bornCountryCode')
        born_country = laureate.get('bornCountry')
        if born_country_code and born_country:
            birth_countries.add((born_country_code, born_country))

    birth_countries_sorted = sorted(list(birth_countries))

    print(f"cats_count={len(categories_sorted)} first={categories_sorted[0]} last={categories_sorted[-1]} sorted_unique=True")
    print (f"names_count={len(full_names_sorted)} first={full_names_sorted[0]} last={full_names_sorted[-1]} sorted_unique=True")
    print(f"countries_count={len(birth_countries_sorted)} first={birth_countries_sorted[0]} last={birth_countries_sorted[-1]} sorted_unique=True")