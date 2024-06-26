#WAP to read a tuple from user and check  prime or not for each value
data=tuple(input("Enter data:"). split(","))
for index in data:
    value=int(index)
    count=0
    for x in range(2, value):
        if value%x==0:
            count+=1
    if(count>0):
        print(f"{value} is prime")       