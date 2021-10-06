
import random
numberOfStreaks = 0
# h_count = 0
# t_count = 0
for exp_num in range(10000):
    li = []
    string = ''

    for i in range(100):
    	li.append(random.choice(['H', 'T']))
    string = string.join(li)

    h_count = string.count("HHHHHH")
    t_count = string.count("TTTTTT")
    count = h_count + t_count
    numberOfStreaks += count

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))

'''

#Method 2
import random
numStreaks = 0
test = 0
flip = []

#running the experiment 10000 times

for exp in range(10000):
    for i in range(100): #list of 100 random heads/tails

        if random.randint(0,1) == 0:
            flip.append('H')
        else:
            flip.append('T')

    for j in range(100): #checking for streaks of 6 heads/tails

        if flip[j:j+6] == ['H','H','H','H','H','H']:
            numStreaks += 1
        elif flip[j:j+6] == ['T','T','T','T','T','T']:
            numStreaks += 1
        else:
            test += 1 #just to test the prog
            continue
print (test)
chance = numStreaks / 10000
print("chance of streaks of 6: %s %%" % chance )


#MEthod 3
import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    hundredList = []
    streak = 0
    for i in range(100):
        hundredList.append(random.choice(['H','T']))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(hundredList)):
        if i == 0:
            pass
        elif hundredList[i] == hundredList[(i-1)]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
            break
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

'''
