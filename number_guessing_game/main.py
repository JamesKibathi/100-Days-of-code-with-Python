import random

number = random.randint(0,100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100"))
    guesses +=1