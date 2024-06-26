#Write a function display_words() in python to read lines from a text file "story.txt" and display those words, which are less than 4 characters.
# Write a function in python to readlines from a test file "notes.txt". your function should find and display the occurence of the word "the"
file = open("story.txt","r")
data = file.readlines()
count = 0
for line in data:
    words = line.split()
    for word in words:
       if len(word) < 4:
            print(word)
        