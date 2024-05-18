# the data which is being assigned to the variables are called as literal or we can say , Literals are raw data which is being assigned to the variables or constants.

###################Numerical Literals #############################
# there are basically three types of numerica literals and they are : Integer, float and complex

# #Integer
# a = 30

# # float 
# b = 3.14

# #complex

# c = 10 + 1j
# #checking the literal types of c
# print(type(c)) 
# #we can use .real and .imag to generate real and imaginary components of complex number.
# print(a , b , c.real , c.imag)

###############string literals ####################
# we can use single , double and triple quotationns to assign string literals. generally single and double are used for single line and triple quotations are used for multiple lines .
# single = " I am single !"
# chapri = ' I am also single yrr'
# multiline = '''Chinta nali kta ho 
#                 Tero daiko tannai kt xa
#                 1.papaki pari
#                     2.chimeki ko chori'''
# print(single)
# print(chapri)
# print(multiline)

################Boolean literals ###################
# boolean value true ra false hunxa true lai 1 ra false lai 0 vanxa 
# boolean1 = (1 == True)
# boolean2 = (2 == False)

# num = 20
# age = 20

# x = True + 10
# y= False + 10

# print(boolean1)
# print(boolean2)

# print(num==age)

# print ("value of x and y: ", x , y)

###########Special Literals ##########################
aalu = "available"
pyaj = None 

def items(x):
    if x == aalu :
        print("aalu: ",aalu)
    else:
        print('aalu',pyaj)

items(aalu)
items(pyaj)