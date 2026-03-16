import json
import os

class Budget:
    def __init__(self, json_path=None):
        # private attribute
        self._transactions = []

        # Case 1: no json_path → start empty
        if json_path is None:
            return

        # Case 2: file does not exist
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"File not found: {json_path}")

        # Case 3: read + parse JSON
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            raise  # re-raise JSONDecodeError

        # Case 4: must contain "transactions" key
        if "transactions" not in data:
            raise ValueError('JSON must contain a "transactions" key')

        # Case 5: "transactions" must be a list
        if not isinstance(data["transactions"], list):
            raise ValueError('"transactions" must be a list')

        # Case 6: import using same rules as add_transactions (Task 03)
        self.add_transactions(data["transactions"])

    # Task 03 API (unchanged)
    def add_transactions(self, transactions_list):
        for value in transactions_list:
            if value != 0:  # ignore zeros
                self._transactions.append(value)

    # Task 01 output rules
    def print_transactions(self):
        for tx in self._transactions:
            if tx > 0:
                print("You received " + f"{tx:.2f}" + " euros")
            elif tx < 0:
                print("You spent " + f"{abs(tx):.2f}" + " euros")

    # Task 02 output rules
    def print_sorted_transactions(self):
        sorted_tx = sorted(self._transactions)
        for tx in sorted_tx:
            if tx > 0:
                print("You received " + f"{tx:.2f}" + " euros")
            elif tx < 0:
                print("You spent " + f"{abs(tx):.2f}" + " euros")
