#program to find the largest number from the list
list = [99,87,12,8,43,46,112,89]
largest = 0
#we should use loop to compare every element
for x in range(len(list)):
    if (list[x]>largest):
        largest = list[x]
print("The largest number from the list is ",largest)

