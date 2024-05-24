# WAP that accepts variable number of arguments from user and finds factorial of each number and then displays factorial of every number.
def factorial(*num):
    #using for loop to take one by one integer
    for value in num:
        fact=1
        for i in  range(1,value+1):
            fact=fact*i
        print(fact)
factorial(1,2,4,5)        
        