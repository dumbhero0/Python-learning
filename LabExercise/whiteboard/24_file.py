#Delete both students.csv and data.txt using os module
import os

file_paths = ["students.csv", "data.txt"]

for file_path in file_paths:
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")
