'''Take a guess
10
Your guess is too low
Take a guess
15
Your guess is too low
Take a guess
17
Your guess is too high
Take a guess
16
Good job! You guessed my number in 4 guesses! '''

#Guess the number game
import random
secretNum = random.randint(1, 10)
print("I am thinking of a number between 1 to 20")

#Asking user to enter a number
for guessesTaken in range(1, 10):
    guess = int(input("Take a guess:"))
    if guess < secretNum:
        print("Guess is too low")
    elif guess > secretNum:
        print("Guess is too high")
    else:
        break
if guess == secretNum :
    print("Good job! you guessed my number in "+ str(guessesTaken) + "Guesses!")
else:
    print("Nope! the nuber i was thinking of was:" , secretNum)
