birthdays = {"vijju" : "may 5", "sagar": "june 30", "dhruv" : "sept 14", "pradeep" : "jan 16"}

while True:
    print("Enter a name to see their birthday (blank string to quit) :")
    name = input()

    if name == '':
        break
    if name in birthdays:
        print(name + "'s birthday is on :" + birthdays[name])
    else:
        print("The name not in the list")
        print("please enter the birth day : ")
        bday = input()
        birthdays[name] = bday
        print("The birthdays db is updated")

print(birthdays)

#the updated data will last as soon as we quit the program.
# We should learn to copy and access data into the files
