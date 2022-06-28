import random

print("Number guessing game")

print("Guess a number (between 1 and 9):")

# RANDOM INTEGER
number = random.randint(1, 9)

chances = 0

while chances < 5:

    # Enter a number between 1 to 9
    guess = int(input("Enter your guess -> "))

    if guess == number:
        print("Congratulations! YOU WON! :D")
        break
    elif guess > number:
        print("Your guess was way too high :(", guess)

    else:
        print("Your guess was way too low :(", guess)
    chances += 1


if not chances < 5:
    print("YOU LOST :( The number was", number)

    # Made By Kartavya Oberoi :)
    # more examples are macOS and Linux
    #They provide a UI (User Interface)
    