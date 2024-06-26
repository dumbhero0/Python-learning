# Write a function in python to count the words "this" and "these" presents in a text file "article.txt"[Note that "this" and "these" are compplete words]
file = open("article.txt","r")
data = file.readlines()
count = 0
for line in data:
    words = line.split()
    for word in words:
      if (word.lower() == "this") or (word.lower() == "these"):
            count+=1
print(count)