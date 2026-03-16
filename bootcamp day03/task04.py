from mongoengine import connect
connect(db="nobel_database", host="localhost", port=27017)
from task02 import Prize

def display_shared_peace_NP(db):
    shared_peace = []

    if __name__ == "__main__":
     for prize in Prize.objects(category="Peace"):

        if prize.laureates and len(prize.laureates) == 2:
            names = []

            for l in prize.laureates:
                if hasattr(l, "surname") and l.surname:
                    fullname = f"{l.firstname} {l.surname}".strip()
                else:
                    fullname = l.firstname.strip()
                names.append(fullname)

            names.sort(key=str.lower)

            result.append((str(prize.year), names))


    result.sort(key=lambda x: x[0])

    print(result)
    return result
    
display_shared_peace_NP(None)