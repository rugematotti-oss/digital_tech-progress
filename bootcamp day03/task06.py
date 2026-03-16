def display_multiple_laureates(db):
    multiple_laureates = []
    for prize in Prize.objects:
        if prize.laureates and len(prize.laureates) > 1:
            names = []
            for l in prize.laureates:
                if hasattr(l, "surname") and l.surname:
                    fullname = f"{l.firstname} {l.surname}".strip()
                else:
                    fullname = l.firstname.strip()
                names.append(fullname)
            names.sort(key=str.lower)
            multiple_laureates.append((prize.year, prize.category, names))
    multiple_laureates.sort(key=lambda x: x[0])
    print(multiple_laureates)
    return multiple_laureates