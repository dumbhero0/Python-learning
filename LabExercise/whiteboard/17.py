#In a list delete all items containing other than alphabets .
list = ["Sonam",1, "ham1",7,"masu"]
list1=[]
for value in list:
    if isinstance(value,str) and value.isalpha():#isinstance(Value,str) is used to check if the value is string
        list1.append(value)
print(list1)   
      

