while True:
    name = input("who are you ?")
    if name != "joe":
        continue
    print("Hello joe! What is your password?(It is a fish!)")
    password = input()
    if password == "sword fish" :
        break
print('Access Granted!')
