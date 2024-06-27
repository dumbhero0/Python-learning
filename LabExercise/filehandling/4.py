# Write a function in python to readlines from a test file "notes.txt". your function should find and display the occurence of the word "the"
def findThe():
    file = open("notes.txt","r")
    data = file.readlines()
    count = 0
    for line in data:
        words = line.split()
        for word in words:
            if word.lower() == "the":
                count+=1
    print(f"Total number:{count}")
findThe()