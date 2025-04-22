import random

number_to_guess = random.randint(1, 100)
guess_counter = 0
max_attempts = 5

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess:
    guess_counter += 1
    if guess_counter == max_attempts:
        print(f"Sorry! You've reached the maximum number of attempts. The number was {number_to_guess}.")
        break

    if guess < number_to_guess:
        print("Higher Your Guess! & Try Again")
    else:
        print("Lower Your Guess! & Try Again")

    guess = int(input("Guess a number between 1 and 100: "))

else:
    print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
