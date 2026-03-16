def display_chemistry_NP(db, country: str): 
    chemistry_laureates = set() 
    for prize in Prize.objects(category="Chemistry"): 
        if prize.laureates: 
            for laureate in prize.laureates: 
                if hasattr(laureate, "bornCountry") and laureate.bornCountry and laureate.bornCountry.lower() == country.lower(): 
                    if hasattr(laureate, "surname") and laureate.surname: 
                        fullname = f"{laureate.firstname} {laureate.surname}".strip() 
                    else: 
                        fullname = laureate.firstname.strip() 
                    chemistry_laureates.add(fullname) 
    sorted_chemistry_laureates = sorted(chemistry_laureates, key=lambda x: x.lower()) 
    print(sorted_chemistry_laureates) 
    return sorted_chemistry_laureates