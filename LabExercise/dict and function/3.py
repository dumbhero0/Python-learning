#write a program to read 6 numbers and create a dictionary having keys even and odd . dictionary's value should be stored in list . Y
#our dictionary should be like {"EVEN":[8,10,64], "ODD":[1,3,5]}

dic={"EVEN":[],"ODD":[]}
inte=[1,2,3,4,5,6,7,8,9,10]
# var=input("Enter the number")
for value in inte:
    if value%2==0:
        dic["EVEN"].append(value)
    else:
        dic["ODD"].append(value)
print(dic)