"""A number-guessing game."""

# greet player
# get playe rname
# choose random number
# repeat until number is guessed:
# if incorrect, give hint, add to guess counter
# if correct, congratulate

import random

user_name = input("Hi, what's your name?\n>")
print("{}, I'm thinking of a number between 1 and 100. Try to guess my number.".format(user_name))


random_number = random.randint(0, 100)

print(random_number)

counter = 1

while True:
    while True:
        try:
            user_guess = int(input("Your guess?\n>"))
            break
        except ValueError:
            print("That wasn't an integer! Try again.")

    if user_guess == random_number:
        break

    if user_guess not in range(1, 101):
        print("That is not a valid answer, please guess again.")
    elif user_guess > random_number:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")
    counter += 1

print(f"Congratulations {user_name} You guessed the number in {counter} tries!")
