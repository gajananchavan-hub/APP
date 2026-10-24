
import csv
import re

filename = "customers.csv"

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

print("Customer Records:")

for customer in customers:
    print(customer)

account_no = input("\nEnter Account Number to search: ")

# Validate account number
if not re.fullmatch(r"\d{10}", account_no):
    print("Invalid Account Number. Account number must contain 10 digits.")
else:
    found = False

    for customer in customers:
        if customer["Account Number"] == account_no:
            print("\nCustomer Found:")
            for key, value in customer.items():
                print(key + ":", value)
            found = True
            break

    if not found:
        print("Customer not found.")
