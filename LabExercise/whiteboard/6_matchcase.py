x = 0
while not (1 <= x <= 7):
    x = int(input("Enter the Day number to know the name of the day: "))
    match x:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Please enter a number from 1 to 7")
