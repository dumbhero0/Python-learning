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

#String concatenation
#We used + to concatenate different strings
a = "Hello"
b = "Sathi"
c = a + b
print(c)

#Adding space between two string:
a = "Hello"
b = "Sathi"
c = a + " " +b
print(c)

#Capitalizing the first character to uppercase
a = "this is demo"
print(a.capitalize())

#convert string in to lowercase
m = "Hi Sathi"
print(m.casefold())
print(m.lower())

#convert string in to uppercase
msg =" good morning dear "
print(msg.upper())

#checking if the string is lowercase
string = "this is lowercase"
print(string.islower())

#checking if the string is uppercase
print(string.isupper())

#counting the character in the string
a = " this is this is this is"
print(a.count("this"))

#syntax: string.center(kati length ko string banaune)
a = "banana"
b=a.center(20)
print(b)
print(len(b))

#