import random

number = random.randint(0,100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100\n"))
    guesses +=1

    if guess == number:
        print(f"Congratulations, you guessed the number in {guesses} guesses!")
        break
    elif guess < number:
        print(f"Too low, guess higher!")
    else:
        print(f"Too high, guess lower!")        