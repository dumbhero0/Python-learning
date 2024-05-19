#There are some string methods to perform specific task
#Modifying strings
#Upper case
a = "Hello, world"
print(a.upper())

#Lower case
print(a.lower())

#Remove Whitespace
a ="Hello, world!  "
print(a.strip())

#Replacing string
a = "Can do"
#Syntax: string.replace("string to replace","String that replace")
print(a.replace("Can","can't"))

#Spliting string
a = "there are four words"
print(a.split(" "))
print("The numbers of words in string ",len(a.split(" ")))

#