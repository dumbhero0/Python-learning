#check for two variables address and also display the memory address of both variables
a = 10
b = 11
c = 10

print("a and b are same : ",a is b)
print ("a and c are same : ",a is c)
print("the memory address of a :" , id(a))
print("the memory address of b :" , id(b))
print("the memory address of c :" , id(c))