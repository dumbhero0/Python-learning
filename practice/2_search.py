#program to search in list whether it contains the multiple of 5 and 3 (*using else claues in for loop)
list = [3,5,6,9,8,11,15]
for index in range(len(list)):
    if(list[index]%3==0 or list[index]%5==0):
        print("yes ! there is multiples of 5 or 3 in list")
        break
    else:
     print("No ! there is not any multiples of 5 or 3")