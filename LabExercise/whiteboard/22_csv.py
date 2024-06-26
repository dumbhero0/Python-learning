#Rename the file data.csv to students.csv using os module.
import os

if os.path.exists("data.csv"):
    os.rename("data.csv", "students.csv")
    print("File renamed successfully.")
else:
    print("data.csv does not exist.")
