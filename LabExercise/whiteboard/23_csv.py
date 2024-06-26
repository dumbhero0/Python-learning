#Display all data of students.csv file
import csv
with open ("students.csv", mode ="r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)