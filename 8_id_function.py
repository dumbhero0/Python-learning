#id() is used to return a unique identification value of the object stored in the memory.it generate unique identification number for uniqe value
#it follows the concept of linked, if the different variables have same value it can store in same location instead of using different location like in other programming language
a = 10
b = a
c = 15 - 5
d = 5 + 5
e = 2 * 5
print("id of a:",id(a))
print("id of b:",id(b))
print("id of c:",id(c))
print("id of d:",id(d))
print("id of e:",id(e))

'''
Output 
id of a: 10815496
id of b: 10815496
id of c: 10815496
id of d: 10815496
id of e: 10815496
'''
#the output of all the above syntax will be same because all the variables have same data.
#lets change different value for different variables
m = 10
n = 11
o = 24
print("id of m:",id(m))
print("id of n:",id(n))
print("id of o:",id(o))
'''
output:
id of m: 10815496
id of n: 10815528
id of o: 10815944
'''
#[note: id(11) is the next block afer id(10) in the memory location.python integers values are 4 bytes(32 bits) which is exact difference between id of 11 and 10 in the output section.]
##########################################################
#Python id() functions on immutable objects :
#In list and dictionaries , the id() function allocates different identity numbers even the values are same

list1 = [1,2,3,4]
list2 = [1,2,3,4]
dict1 = {'sonam':12 , 'cybercena':15}
dict2 = {'sonam':12 , 'cybercena':15}

print("id of list1 :",id(list1))
print("id of list2 :",id(list2))
print("id of dict1:",id(dict1))
print("id of dict2 :",id(dict2))

'''
outputs:
id of list1 : 140397951482816
id of list2 : 140397945865408
id of dict1: 140397951481792
id of dict2 : 140397951532928
even with same value dictionaries and list have different identity numbers . and same case applied in custom object also.
'''