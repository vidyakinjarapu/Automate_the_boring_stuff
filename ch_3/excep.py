
def spam(num) :
    try:
        return 42 / num
    except ZeroDivisionError:
        print("We cannot devide with zero")

print(spam(2))
print(spam(0))
print(spam(4))


'''
#Handling exception in the calling section
def spam(num):
    return 42 / num

try:
    print(spam(2))
    print(spam(0))
    print(spam(4))
except ZeroDivisionError:
    print("Error : Invalid Argument")
'''
