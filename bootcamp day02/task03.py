from unicodedata import name


class Athlete:
    def __init__(self, name, country, birthdate):
        self._name = name
        self._country = country
        self._birthdate = birthdate
        self._records = []

    def set_name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = new_name.strip()

    def set_country(self, new_country):
        if not isinstance(new_country, str) or not new_country.strip():
            raise ValueError("Country must be a non-empty string")
        self._country = new_country.strip()

    def set_birthdate(self, new_birthdate):
        if not isinstance(new_birthdate, str) or not new_birthdate.strip():
            raise ValueError("Birthdate must be a non-empty string")
        self._birthdate = new_birthdate.strip()

    def add_record(self, championship_name, rank):
        self._records.append((championship_name, rank))

    def print(self):
        
        print(f"My name is : {self._name}, from {self._country}")
        print(f"Birthdate: {self._birthdate}")

