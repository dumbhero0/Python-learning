#Write a function in python to count and display the total numbers of words in a text file.
def TotalNum():
    file = open("poem.txt","r")
    data = file.readlines()
    words=[]
    count = 0
    for line in data:
        word=line.split()
        for i in word:
            count+=1
    print(count)
TotalNum()