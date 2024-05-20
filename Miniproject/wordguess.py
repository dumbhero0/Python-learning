import random

# Assuming countryname.py contains an array named 'countryname' with country names
import countryname as c

name = input("What's your name: ")
print("Good luck!", name)

# Importing name of the countries from the file countryname.py
countries = c.countryname

# Choosing a random country name
word = random.choice(countries).lower()
print("Guess the country: ")

guesses = ""
turns = 12

while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    print()  # For a new line after each round of guesses

    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break
    
    guess = input("Guess a character: ").lower()
    
    if guess in guesses:
        print("You already guessed that character.")
        continue

    guesses += guess
    
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, 'more guesses')
        
        if turns == 0:
            print("You lose")
            print("The word was:", word)
