#Wap to read two numbers (say x and y ) and perform following operations:
# a.Display binary equivalent of the numbers
# b.Perform bitwise AND, OR and XOR operations and display their results in binary format
# c.Perform once complement of x and display the result in binary format
# d.Left shift the x by 3 positions and display the result in binary format
# e.Left shift the y by 2 positions and display the result in binary format

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(f"The binary value of x and y is {bin(x)} and {bin(y)} respectively.")
print(f"The AND operation between  {x} and {y} is: {bin(x & y)}")
print(f"The OR operation between {x} and {y} is: {bin(x|y)}")
print(f"The XOR operations between {x} and {y} is: {bin(x^y)}")

print(f"The once complement of x is: {bin(~x)}")
print(f"The left shift on {bin(x)} by 3 bits is {bin(x<<3)}")
print(f"The left shift on {bin(y)} by  2 bits is {bin(y<<2)}")