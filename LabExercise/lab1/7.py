#WAP to count odd and even numbers in a list.
list = [1,2,7,9,6,12]
odd=0
even=0
for num in list:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(f"there are {even} even and {odd} odd numbers.")
