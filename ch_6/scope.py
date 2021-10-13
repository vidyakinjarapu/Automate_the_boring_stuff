def outer_function():
    x = 11

    def inner_function():
        nonlocal x
        x = 22
        print('Inner x:', x)
    inner_function()
    print('Outer x:', x)

outer_function()
# print(x)
