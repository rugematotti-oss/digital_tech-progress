def print_sorted_transactions(transactions_list):
    sorted_tx = sorted(transactions_list)
    for transaction in sorted_tx:
        if transaction > 0:
            print("You have received " + f"{float(transaction):.2f}" + " Euros")
        elif transaction < 0:
            print("You have spent " + f"{abs(transaction):.2f}" + " Euros")


