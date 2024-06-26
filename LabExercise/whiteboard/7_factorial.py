#WAP to create a function that accepts variable numbers of arguments and find the factorial of each . then display all results.
def factorial(*num):
    #using for loop to take one by one integer
    for value in num:
        fact=1
        for i in  range(1,value+1):
            fact=fact*i
        print(fact)
factorial(1,2,4,5)        
        