#WAP to extract all prime numbers form a list using filter tool.
def prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

nums = [0,1,2,3,4,6,7,8,9,13]
prime_numbers = list(filter(prime,nums))
print(prime_numbers)