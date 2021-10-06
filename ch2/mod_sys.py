import sys
while True:
    response = input("Please enter exit to exit: ")
    if response == "exit" :
        sys.exit()
    print("You typed "+ response + "as a response not exit")
