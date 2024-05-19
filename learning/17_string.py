#Illustrate string as array
a = "this is demo"
print(a[0])
print("\n")
#looping through string
for x in "Apple":
    print(x)
print("\n")

#string length
a = "hello sathi"
print(len(a))

##checking string 

txt = "My country Nepal"
print ("Nepal" in txt)
print(txt)

###check if not
text = "this is demo"
print("draft" not in text)

#This is the section where we are going to learn about slicing the strings
#Syntax: string[start:end]
#printing the character from index 2 to index 5
b = "01234567"
print(b[2:5])

#Slicing from the start:it takes certain number of character from starting
# syntax: string[:character's number']
a = "01234567"
print(a[:5])

#slicing to the end:
# by leaving the end index , the range will go to the end 
#Agadi ko index jati character xodxa baki slice garxa
x = "01234567"
print(x[2:])

#Negative indexing
# syntax:string[x:y] jasma x matlab paxadi bata x number of character gannera tyo position ma puginxa ani y bhaneko paxadi katiota character xodney bhanne ho
y = '01234567891909'
print(y[-4:-2])
