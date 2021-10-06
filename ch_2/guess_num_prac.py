import random
c_guess = random.randint(1, 20)
print("I'm thinking of a number between 1 to 20")

for i in range(0, 5):
    u_guess = int(input("Enter a number between 1 to 20 : "))
    if c_guess == u_guess :
        print("Your guess is correct.")
        print("You guessed in " + str(i) + " number of guesses")
    elif c_guess < u_guess :
        print("Your guess is too high! ")
    elif c_guess > u_guess :
        print("Your guess is too low! ")
    else:
        break
print("Your guesses are over! The number i was thinking : "+ str(c_guess))
