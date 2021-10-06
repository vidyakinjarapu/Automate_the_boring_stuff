"""
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
"""
import random, sys
print("ROCK, PAPER, SCISSORS")
Wins = 0
Losses = 0
Ties = 0

while True:
    print("%s wins, %s losses, %s ties" %(Wins, Losses, Ties))
    while True:
        user_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit : ")
        if user_move == 'q' :
            sys.exit()
        elif user_move == 'r' or user_move == 'p' or user_move == 's':
            break
        print("Please enter ony one of r, p, s")

    #Printing the user's move.
    if user_move == 'r':
        print('ROCK verses...')
    elif user_move == 'p':
        print('PAPER verses...')
    else :
        print('SCISSORS verses...')

    #printing what computer choose
    li = ['r', 'p', 's']
    comp_move = random.choice(li)
    if comp_move == 'r':
        print('ROCK')
    elif comp_move == 'p':
        print('PAPER')
    else :
        print('SCISSORS')

    #Game to find wind and Losses
    if user_move == comp_move :
        print("It's a tie")
        Ties += 1
    elif user_move == 'p' and comp_move == 'r':
        print("You win")
        Wins += 1
    elif user_move == 'p' and comp_move == 's':
        print("You lost")
        Losses += 1
    elif user_move == 'r' and comp_move == 'p':
        print("You lost")
        Losses += 1
    elif user_move == 'r' and comp_move == 's':
        print("You win")
        Wins += 1
    elif user_move == 's' and comp_move == 'r':
        print("You lost")
        Losses += 1
    elif user_move == 's' and comp_move == 'p':
        print("You win")
        Wins += 1
