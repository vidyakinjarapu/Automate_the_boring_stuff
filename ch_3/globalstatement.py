def spam():
    #The assignment is done to the globally scoped variable
    #It change the global variable to eggs to 'spam'
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
