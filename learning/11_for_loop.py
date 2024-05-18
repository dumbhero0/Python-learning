#python for loops is used to iterating the set of statements , datastructure , or iterable objects.by default conditonal loop hunna hamile aru languagema for each use gare jastai gari loop lagauxau.
'''Syntax:
    for iterating_var in seq:
        statement(s)
    '''

#example of for loops

fruits = ['apple','banana','mango','grapes','orange']
for x in fruits:
    print(x)

#sum of numbers in list
num = [1,4,5,6]
sum = 0
for i in num:
    sum = sum + i
print('the sum is :',sum)

#Iterating by sequence indexing
fruits = ['apple','banana','mango','grapes','oranges']
for index in range(len(fruits)):
    print(fruits[index])

#using range() function
# syntax : range(start, stop, step_size)
# program to print a range of numbers 
for i in range(5):
    print(i)

##################################################################
# for loop with else 

dislike_choice = 'worst'
genre ={'good':'mango','good':'banana','bad':'grapes','better':'mango'}

for s in genre:
    if s == dislike_choice:
        print('I do not like',genre[s])
        break
else:
    print('worst genre not found')

########################################################################
#Nested for loop
rows = int(input("Enter no of rows: "))
for i in range(rows+1):
    for j in  range(i):
        print('*',end = ' ')
    print()
########################################################
