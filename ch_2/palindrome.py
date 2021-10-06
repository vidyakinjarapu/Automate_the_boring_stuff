# Have the same word forward and backward
#eg: Racecar -->  racecaR

def palindrome(word):
    word = word.lower()
    li = list(word)
    rev_li = list(reversed(word))
    print(rev_li)

    if li == rev_li :
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome!")

word = input("Enter a word to test : ")
palindrome(word)
