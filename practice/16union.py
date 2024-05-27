#1. create two lists and generate another list having items that occurs in both list.
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,1]
list=[]

for value in list1:
    if value in list2:
        list.append(value)
print(list)


    
