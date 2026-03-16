from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    IntField,
    ListField,
    EmbeddedDocumentField,
    connect
)

# Connect first
connect("nobel_database", host="localhost", port=27017)


class Country(Document):
    name = StringField(required=True)
    code = StringField()


class Laureate(EmbeddedDocument):
    id = StringField()
    firstname = StringField()
    surname = StringField()


class Prize(Document):
    year = IntField(required=True)
    category = StringField(required=True)
    laureates = ListField(EmbeddedDocumentField(Laureate))


if __name__ == "__main__":

    # Query physics prizes
    for prize in Prize.objects(category="physics"):
        print(prize.year, prize.category)

    # Query Curie through Prize (NOT Laureate.objects)
    for prize in Prize.objects:
        for l in prize.laureates:
            if l.surname == "Curie":
                print(l.firstname, l.surname)
