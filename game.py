"""A number-guessing game."""

# greet player
# get player name
# choose random number
# repeat until number is guessed:
# if incorrect, give hint, add to guess counter
# if correct, congratulate

import random
user_name = input("Hi, what's your name?\n>")
best_score = 100
human_or_computer = input("You can guess numbers, or the computer can guess. Type 'Y' for you or 'N' computer.\n")


def computer_game_play():
    """Computer guessing numbers and user responding 'too high' or 'too low'"""

    print("Give me a range! Pick a starting number and an ending number.")
    start_num = int(input("Start number >"))
    end_num = int(input("End number >"))

    random_number = random.randint(start_num, end_num)

    print(random_number)

    while True:
        random_guess = random.randint(start_num, end_num)
        print(f"Is the number {random_guess} ?")
        if random_guess > random_number:
            input("> ")
            # resets range so you can't make a higher guess than previous
            end_num = random_guess - 1
        elif random_guess < random_number:
            input("> ")
            # resets range so you can't make a lower guess than previous
            start_num = random_guess + 1
        elif random_guess == random_number:
            break
    print("Wow! I guessed the number! Woohoo!")


def game_play(score):
    """User guessing numbers and computer responding 'too high' or 'too low'"""

    print("The score is", score)
    print("You get to set your own range. Pick a starting number and an ending number.")
    start_num = int(input("Start number >"))
    end_num = int(input("End number >"))

    print(f"{user_name}, I'm thinking of a number between and including {start_num} and {end_num}. Try to guess my number.")

    random_number = random.randint(start_num, end_num)

    print(random_number)

    counter = 1

    while True:
        while True:
            # checks for an integer input
            try:
                user_guess = int(input("Your guess?\n>"))
                break
            except ValueError:
                print("That wasn't an integer! Try again.")

        if user_guess == random_number:
            print(f"Congratulations {user_name} ! You guessed the number in {counter} tries!")
            break
        if counter > 10:
            print("That's all the guesses you get.")
            break
        if user_guess not in range(1, 101):
            print("That is not a valid answer, please guess again.")
        elif user_guess > random_number:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")
        counter += 1

    # score conversions based on difficulty/range length

    if len(range(start_num, end_num)) <= 50:
        counter = int(counter*2)
    elif len(range(start_num, end_num)) > 100:
        counter = int(counter/2)

    # if new best score is set:

    if counter <= score:
        score = counter
        print("Congrats! That's a new best score!")

    # prompting for play again

    new_game = input("Do you want to play again (Y/N)?\n>")
    if new_game.upper() == "N":
        print("Ok, bye.")
    elif new_game.upper() == "Y":
        game_play(score)
    else:
        print("That is not a valid answer. Good bye.")

# Y if human is guessing, N if computer is guessing
if human_or_computer.upper() == "Y":
    game_play(best_score)
elif human_or_computer.upper() == "N":
    computer_game_play()
else:
    print("Invalid entry. Good bye.")
