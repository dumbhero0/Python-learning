#WAP that reads a string from user and then finds number of alphabets, digits,and special characters in string.
str = input("Enter the string: ")
alphabet=0
digit=0
special_character=0
for char in str:
    if char.isalpha():
        alphabet+=1
    elif char.isdigit():
        digit+=1
    else:
        special_character+=1

print(f"Total Alphabets:{alphabet}") 
print(f"Total digit:{digit}")
print(f"Total Special characters: {special_character}")
 
