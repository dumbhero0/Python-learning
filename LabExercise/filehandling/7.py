#Write a function in python to count words in a text file those are ending with alphabet"e".
file = open("article.txt","r")
data = file.readlines()
count = 0
for line in data:
    words = line.split()
    for word in words:
        word=word.strip()
        if word.lower().endswith('e'):
            count+=1
print(count)