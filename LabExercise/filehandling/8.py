#Write a function in python to count uppercase character in a text file.
def countUpper():
    file = open("poem.txt", "r")
    data = file.readlines()
    count = 0

    for line in data:
        for ch in line: 
            if ch.isupper():
                count += 1

    print(f"Total uppercase: {count}")

    file.close() 
countUpper()