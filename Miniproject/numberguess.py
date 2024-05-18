import random

def guess_game():
    num = random.randint(1,100)
    attempts = 0
    guess = None
    print("Welcome to the Guessing Game!")
    print("I have think a number between 1 and 100.\n Try to Guess it !\n ")

    while (attempts<=5 and guess != num):
        guess=int(input("Enter your guess: "))
        attempts+=1

        if(1>guess>100):
            print("please Enter number between 1 to 100")
        elif guess > num:
            print("Too much ! Try again.")
        elif guess < num:
            print("Too low ! Try again.")
        else:
            print("Congratulations! you guessed it")
guess_game()