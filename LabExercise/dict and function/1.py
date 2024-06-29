students ={}
print("Enter name and roll no of students. Enter \"000\" to exit")
while True:
    a=input("name: " )
    if a=="000":
        break
    b=input("Roll No: ")
    students[a]=b

# print all key and value
for key,value in students.items():
    print(f"Name: {key}  RollNo: {value}")

# Delete
del students["tarjan"]

# Add new item
a=input("name: " )
b=input("Roll No: ")
students[a]=b

for key,value in students.items():
    print(f"Name: {key}  RollNo: {value}")

#MOdify name of existing student
old_value=students.pop("sonam")
students["Taarzaaan"]=old_value

for key,value in students.items():
    print(f"Name: {key}  RollNo: {value}")