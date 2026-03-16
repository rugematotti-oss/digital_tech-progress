def display_french_NP(db):
    french_laureates = set()
    for prize in Prize.objects:
        if prize.laureates:
            for laureate in prize.laureates:
                if hasattr(laureate, "bornCountry") and laureate.bornCountry and laureate.bornCountry.lower() == "france":
                    if hasattr(laureate, "surname") and laureate.surname:
                        fullname = f"{laureate.firstname} {laureate.surname}".strip()
                    else:
                        fullname = laureate.firstname.strip()
                    french_laureates.add(fullname)
    sorted_french_laureates = sorted(french_laureates, key=lambda x: x.lower())
    print(sorted_french_laureates)
    return sorted_french_laureates