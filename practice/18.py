#create two lists and merge them.also delete 2nd item after merge then add two items after 5th index
list1=["masu","achar","dal","Bhat"]
list2=[1,2,3,4,5]
for value in list2:
    list1.append(value)
list1.remove(list1[1])#removing 2nd item which lies in 1th index 
list1[6:6]=["A","B"] #adding two item after 5th index 
print(list1)