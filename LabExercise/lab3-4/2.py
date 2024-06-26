#WAP to reads input from the user and writes it to the file test.txt until user enters bye. Then read and display the content of file.
file = open("test.txt","w")

while True:
    user_input = input("Enter text (enter 'bye' to exit and save):")
    if user_input.lower() == 'bye':
        break
    file.write(user_input + '\n')

file = open("test.txt","r")
content = file.read()
print("\n contents of test.txt :")
print(content)