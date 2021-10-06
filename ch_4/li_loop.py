supplies = ['pen', 'pencil' 'eraser', 'staples']

'''
for i in range(len(supplies)) :
    # print(supplies[i])
    print("The item " + str(i + 1) + " in supplies is :" + supplies[i])

for item in supplies:
    print("the item is " + item)
'''
name = input("Enter the name of the supply to search in the list: ")
if name not in supplies:
    print("I donot have " + name + " in my supplies" )
else:
    print("I have " + name +" in my supplies")
