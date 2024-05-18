#WAP to perform bitwise operation of numbers.
a = int(input("Enter your first number: "))
b = int(input("Enter your Second number: "))
print("The AND operation between a and b is: ",(a & b))
print("The OR operation between a and b is: ",(a | b))
print("The XOR operation between a and b is: ",(a^b))
print("The XNOR operation betweeen a and b is: ",(a^b))
print("The one's compliment of a is: ",~a)

choice=input("\n Do you want to perform shift operation:\n 1.yes  \n 2.No \n")
if(choice!=1):
    x=int(input("By how many bit you want to shift: "))
    print("The leftshift operation of a is: ",bin(a<<x))
    print("The Rightshift operation of a is: ",bin(a>>x))
