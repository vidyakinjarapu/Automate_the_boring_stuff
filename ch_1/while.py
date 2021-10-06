# spam = 0
# if spam < 5 :
#     print("Hello, World!")
#     spam = spam + 1


# spam = 0
# while spam < 5 :
#     print("Hello, world!")
#     spam = spam + 1


# name = ''
# while name != "your name" :
#     print("Please type your name")
#     name = input()
# print("Thank you!")



# #BREAK statement
# while True:
#     print('Please enter nyour name: ')
#     name = input()
#     if name == 'your name':
#         break
# print('Thankyou!')

#CONTINUE statement
while True:
    name = input("Enter your name: ")
    if name != "joe":
        continue
    password = input("Hello joe! What is your password?: ")
    if password == "clown fish":
        break
print("Access has been granted!")
