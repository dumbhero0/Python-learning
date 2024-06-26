#WAP to accept variable number of arguments and return their addition and multiplication
def SumMul(*value):
    sum=0
    mul=1
    for i in value:
        sum+=i
        mul=mul*i
    print("The sum of numbers is: ",sum)
    print("The multiplication of numbers is: ",mul)
            
SumMul(10,20)        
        