###############Advanced level##############
# Create a while loop that simulates a bank account balance. It should repeatedly prompt the user to make deposits and withdrawals until they choose to exit.
i = None
balance = 1000
amount=0
while (1 != 0):
    i = int(input("Enter your choice : \n 1.Depost \n 2.Withdraw \n 3.Exit "))
    match i:
        case 1:
            amount=int(input("Enter the amount you want to deposit : "))
            balance += amount
        case 2: 
            amount = int(input("Enter the amount you want to withdraw : "))
            balance -= amount
        case 3 :
            exit()
    print("your account have : Rs.",balance )