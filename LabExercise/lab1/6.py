#WAP to find second largest from a list of elements without using sorting.
list = [1,9,3,0,7,4,10]
largest=0
second_largest=0
for num in list:
    if num > largest:
        largest=num
for num in list:
    if num < largest and num > second_largest:
        second_largest= num
print(f"largest num is {largest} and second largest num is {second_largest}")

