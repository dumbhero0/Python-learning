#program to  take 3 numbers from user and display largest and smallest numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number:" ))
num3=int(input("Enter the third number: "))

largest = num1
smallest = num1

#finding the largest
if num2 > largest :
    largest = num2
if num3 > largest :
    largest = num3

#finding the smallest 
if num2 < smallest :
    smallest = num2
if num3 < smallest :
    smallest = num3 

print("the largest number is : ",largest)
print("the smallest number is : ",smallest)