##write a prgram that read string from user.YOur program should create a dictionary having key as word length and value is count of 
#word of that length.


dic={}
var=input("Enter a string:")
arry=var.split(" ")
for word in arry:
    dic[word]=len(word)
print(dic)