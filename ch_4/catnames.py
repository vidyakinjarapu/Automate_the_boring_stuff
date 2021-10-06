catnames = []
while True:
    print("Please enter a cat name of cat" + str(len(catnames)) + " (or) enter nothing to print :")
    name = input()
    if name == '' :
        break
    else:
        catnames = catnames + [name]

#printing the cat catnames
print("The cat names are: ")
for i in catnames:
     print(" " + i)
