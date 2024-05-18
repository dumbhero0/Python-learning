#if statement are used for decision making with certain conditions
'''Syntax:
if condition:
    statements(S)
    '''
#python programs to illustrate different if conditions

age = int(input("Enter your age :"))
#by default python take input as string we need to convert its data types
if ( age >= 18):
    print("you can get citizenship")
if (age < 18 ):
    print("you are not qualified")

##########################################################################
#if..else is used to choose chose best among alternative which fit the conditions
''' Syntax :
if condition:
    statement(S)
else:
    statement(S)
    '''

#comparision of weight of two people
kale = 60
gorey = 55

if ( kale > gorey):
    print('Kale is heavier than gorey')
else:
    print('Gorey is heavier than kale')

###########################################################################
#if..elif..else statement is used to choose one option among  multiple option that fit the conditions
'''Syntax:
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(S)
else:
    statement(s)
    '''
#Example of program that used if..elif..else to check the grade of student based on the marks
marks = int(input("Enter marks from 0-100: "))

if (marks >= 90):
    print("You passed with A+ Grade")
elif (marks >= 80 and marks < 90):
    print("you passed with A Grade")
elif(marks >= 70 and marks < 80):
    print("you passed with B+ Grade")
elif( marks >= 50):
    print("you passed with B")
else:
    print("you failed in exam")

###########################################################################
#Python nested if statement 
#program to check if sign of a user entered number 
val = int(input("Enter a number:"))

if val >= 0:
    if val == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is Negative")

 ##############################################################################
#  using if..else as ternary operator
#syntax: task1 if(condition) else task2 
name = 'sonam'
print('hello cybercena') if name == 'cybercena' else print('what is your name , dear ?')
#in the above case or ternary operator it will perform task1 if the condition met else it will perform task 2