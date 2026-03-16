def print_transaction(transactions):
    for transaction in transactions:
        if transaction > 0:
            print(f"You have received {transaction:.2f} Euros")
        elif transaction < 0:
            print(f"You have spent {abs(transaction):.2f} Euros")
