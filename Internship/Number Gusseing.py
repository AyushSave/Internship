import random

number = random.randint(1, 100)

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    number = 35
    if guess > number:
        print("Too high")

    elif guess < number:
        print("Too low")

    else:
        print("Correct! You guessed the number.")
        break
 
