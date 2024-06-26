# Write a function in python to count the numbers of lines from a test file "story.txt" which is not starting with an alphabet "T"
file = open("story.txt","r")
count = 0
for line in file:
    line=line.strip()
    if line and not line.startswith('T'):
        count+=1
print(f"Numbers of lines not starting with 'T':{count}")