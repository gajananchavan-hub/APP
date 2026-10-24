
import csv
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    equipment = list(reader)

print("Sports Equipment Records:")

for item in equipment:
    print(item)

equipment_id = input("\nEnter Equipment ID to search: ")

found = False

for item in equipment:
    if item["Equipment ID"] == equipment_id:
        print("\nEquipment Found:")
        for key, value in item.items():
            print(key + ":", value)
        found = True
        break

if not found:
    print("Equipment not found.")
