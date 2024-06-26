import csv

students = [
    {"Name": "Sonam", "Rollno": 1},
    {"Name": "Ram", "Rollno": 2},
    {"Name": "Muna", "Rollno": 3},
    {"Name": "Teena", "Rollno": 4},
    {"Name": "Hari", "Rollno": 5}
]

with open("data.csv", mode="w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Rollno"])
    
    # Write header row (only needed once)
    writer.writeheader()
    
    # Write each student's data
    for student in students:
        writer.writerow(student)
