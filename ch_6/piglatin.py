'''
* word began with vowel('a', 'e', 'i', 'o', 'u', 'y') -- yay add at the end.
* word begins with a consonant or consonant cluster (like ch or gr) --
    that consonant or cluster is moved to the end of the word followed by ay.
    eg -- name -> amenay
          chair -> airchay
*Output should be:
    My name is AL SWEIGART and I am 4,000 years old.
    Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
'''
message = input("Enter the english message to change it into pig latin: ")
# message = "Hello  buddy good morning! follow 3rd RootH."
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        # print(word)
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #seperate the suffexnonletters
    suffixNonLetters = ""
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    #to change the word if it is in uppercase and append
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()

    #seperate consonants at the start
    prefixConsonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word += "yay"

    #set the word back to upper case or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #add non letters to start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    # print(pigLatin)

#join all words on a space
print(" ".join(pigLatin))
# print(pigLatin)
