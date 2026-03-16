import json
import os


class Budget:
    def __init__(self, json_path=None):
        # _transactions is now a DICTIONARY
        # { "category": [values] }
        self._transactions = {}

        # No JSON file → empty dict
        if json_path is None:
            return

        # File must exist
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"File not found: {json_path}")

        # Load JSON
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            raise

        # Must contain "transactions"
        if "transactions" not in data:
            raise ValueError('JSON must contain a "transactions" key')

        if not isinstance(data["transactions"], list):
            raise ValueError('"transactions" must be a list')

        # Parse categorized transactions
        for entry in data["transactions"]:

            # Each entry must be an object
            if not isinstance(entry, dict):
                raise ValueError("Each transaction entry must be an object")

            # Must contain category and values
            if "category" not in entry or "values" not in entry:
                raise ValueError('Each entry must contain "category" and "values"')

            category = entry["category"]
            values = entry["values"]

            # category must be non-empty string
            if not isinstance(category, str) or not category.strip():
                raise ValueError('"category" must be a non-empty string')

            # values must be list
            if not isinstance(values, list):
                raise ValueError('"values" must be a list')

            # Create category if not exists
            if category not in self._transactions:
                self._transactions[category] = []

            # Append values (ignore zeros)
            for v in values:
                if not isinstance(v, (int, float)):
                    raise ValueError("All values must be numbers")

                if v == 0:
                    continue  # ignore 0

                self._transactions[category].append(v)

    # ==========================
    # METHODS
    # ==========================

    def get_categories(self):
        # Return sorted list of category names
        return sorted(self._transactions.keys())

    # --------------------------

    def print_transactions(self, category=None):

        # Case: specific category
        if category is not None:
            if category not in self._transactions:
                raise KeyError(f"Category not found: {category}")

            for tx in self._transactions[category]:
                self._print_single(tx)
            return

        # Case: category = None → print all
        categories = sorted(self._transactions.keys())
        first_printed = True

        for cat in categories:
            values = self._transactions[cat]

            # Skip empty categories
            if not values:
                continue

            # spacing between categories
            if not first_printed:
                print()

            print(f"[ {cat} ]")

            for tx in values:
                self._print_single(tx)

            first_printed = False

    # --------------------------

    def print_sorted_transactions(self, category=None):

        # Case: specific category
        if category is not None:
            if category not in self._transactions:
                raise KeyError(f"Category not found: {category}")

            sorted_vals = sorted(self._transactions[category])

            for tx in sorted_vals:
                self._print_single(tx)
            return

        # Case: category = None → all categories sorted alphabetically
        categories = sorted(self._transactions.keys())
        first_printed = True

        for cat in categories:
            values = self._transactions[cat]

            # Skip empty categories
            if not values:
                continue

            # spacing between categories
            if not first_printed:
                print()

            print(f"[ {cat} ]")

            # sorted copy (DOES NOT MODIFY _transactions)
            sorted_vals = sorted(values)

            for tx in sorted_vals:
                self._print_single(tx)

            first_printed = False

    @staticmethod
    def _print_single(tx):
        if tx > 0:
            print("You received " + f"{tx:.2f}" + " euros")
        elif tx < 0:
            print("You spent " + f"{abs(tx):.2f}" + " euros")

            myBudget = Budget(" data . json ")
            for category in myBudget.get_categories():
                myBudget.print_sorted_transactions(category)
            print('---')
            myBudget.print_transactions()
