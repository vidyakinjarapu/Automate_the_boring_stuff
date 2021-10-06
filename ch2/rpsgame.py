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

wins = 0
losses = 0
ties = 0

while True:
    print("%s wins, %s losses, %s ties" %(wins, losses, ties))
    while True:
        print('Enter your move: (r)rock, (p)paper, (s)scissors or (q)quit : ')
        playerMove = input()
        if playerMove == 'q' :
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's' :
            break
        print('Type one of r, p, s or q.')


    # Display what player choose
    if playerMove == 'r':
        print('ROCK verses...')
    elif playerMove == 'p':
        print('PAPER verses...')
    elif playerMove == 's' :
        print('SCISSORS verses...')

    # Display what computer choose
    randomNum = random.randint(1, 3)
    if randomNum == 1 :
        computerMove = 'r'
        print('ROCK')
    elif randomNum == 2 :
        computerMove = 'p'
        print('PAPER')
    elif randomNum == 3 :
        computerMove = 's'
        print('SCISSORS')

    #Game rules
    if playerMove == computerMove :
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p' :
        print('You lose')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's' :
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's' :
        print("you lose")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r' :
        print('you win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r' :
        print('you lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p' :
        print('you win')
        wins = wins + 1
