# Task 2: Guess the Number Game 

import random

print("Guess the Number between 1 and 100: ")


intended_number = random.randint(1, 100)

while True:
    number = input("Guess: ")

    if number == 'q':
        print("Quit!")
        break
    
    try:

        guess = int(number)

        if guess > intended_number:
            print("Too much!")
    
        elif guess < intended_number:
            print("Too low!")

        else:
            print("Correct!")
            break
    
    except ValueError:
        print("Invalid input. Please enter a number.")