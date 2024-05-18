#program to check in list whether even index has odd numbers or not.
list = [2 , 4 ,3, 7,4,6,8]
for index in  range(len(list)):
    if (index % 2 == 0 ):
        if(list[index]%2 != 0):
            print("yes there is odd number in even index")
            break
    
else:
    print("No ! there is not any odd number in even index")
