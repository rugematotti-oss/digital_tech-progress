class Budget:
    def __init__(self):
        # private attribute
        self._transactions = []

    # add_transactions method
    def add_transactions(self, transactions_list):
        for value in transactions_list:
            if value != 0:  # ignore zeros
                self._transactions.append(value)

    # print_transactions method (Task 01 rules)
    def print_transactions(self):
        for tx in self._transactions:
            if tx > 0:
                print("You received " + f"{tx:.2f}" + " euros")
            elif tx < 0:
                print("You spent " + f"{abs(tx):.2f}" + " euros")

    # print_sorted_transactions method (Task 02 rules)
    def print_sorted_transactions(self):
        sorted_tx = sorted(self._transactions)
        for tx in sorted_tx:
            if tx > 0:
                print("You received " + f"{tx:.2f}" + " euros")
            elif tx < 0:
                print("You spent " + f"{abs(tx):.2f}" + " euros")
