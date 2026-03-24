import json
import csv

employeejson = {
    "name": "Spongebob",
    "age": 30,
    "position": "Chef"}

employeescsv = [
    ["name", "age", "position"],    
    ["Spongebob", 30, "Chef"],
    ["Patrick", 35, "Manager"],
    ["Squidward", 28, "Cashier"]]

text = "Testing file handling in Python."
file_path1 = "test.txt"
file_path2 = "test.json"
file_path3 = "test.csv"

try:
    with open(file_path1, 'x') as file:
        file.write(text)
        print("Data written to " + file_path1)
except FileExistsError:
    print("File already exists. Please choose a different name.")

try:
    with open(file_path2, 'x') as file:
        json.dump(employeejson, file, indent=4)
        print("Data written to " + file_path2)
except FileExistsError:
    print("File already exists. Please choose a different name.")

try:
    with open(file_path3, 'x', newline="") as file:
        writer = csv.writer(file)
        for row in employeescsv:
            writer.writerow(row)
        print("Data written to " + file_path3)
except FileExistsError:
    print("File already exists. Please choose a different name.")