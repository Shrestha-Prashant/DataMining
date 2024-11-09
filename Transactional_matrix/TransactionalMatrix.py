import pandas as pd

# Reading the data from grocery_dataset.txt file
with open('../../Downloads/grocery_dataset.txt', 'r') as file:
    transactions = [line.strip().split(',') for line in file]

# Extracting and initializing all unique items from all transactions
items = sorted(list(set(item.strip() for transaction in transactions for item in transaction)))
transaction_matrix = pd.DataFrame(0, index=range(len(transactions)), columns=items)

# Filling the transactional matrix with 1s where the item is present in the transaction
for i, transaction in enumerate(transactions):
    for item in transaction:
        transaction_matrix.loc[i, item.strip()] = 1

print("Transactional Matrix: ")
print(transaction_matrix)

# Saving the transactional matrix to a CSV file
transaction_matrix.to_csv('transactional_matrix.csv', index=False)