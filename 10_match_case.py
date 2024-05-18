#Match case statements are used to choose option according to different case. It is just like the swith case in other programming language
'''syntax:
match choice:
    case 0:
        statement(S)
    case 1:
        statement(S)
    case _:
        statement(S)
        '''
#case_ is used for default case

#program to print name of days according to number from 1-7

x = int(input("Enter the Days number to know name of days: "))
match x:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("Friday")
    case 7:
        print("saturday")
    case _:
        print("Please enter number from 1-7")
