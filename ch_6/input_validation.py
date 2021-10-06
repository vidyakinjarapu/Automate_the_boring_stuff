# Verify wether an input has only numbers
while True:
    age = input("Please enter your age: ")
    if age.isdecimal():
        break
    print("Please enter the numbers only for age")

# Check password with only letters and nunmbers
while True:
    password = input("Please enter a password: ")
    if password.isalnum():
        break
    print("Please enter password containing only letters and numbers")
