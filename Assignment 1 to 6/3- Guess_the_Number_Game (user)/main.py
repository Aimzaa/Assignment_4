import random
print("Welcome to the Number Guessing Game! ")

secret_number = random.randint(1, 10)
print("I have a secret number between 1 to 10. Can you guess it? ")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed it! ")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 to 10.")