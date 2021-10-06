ldkddfdlkl, dduifuid8fu'''
word began with vowel -- yay add at the end
word begins with a consonant or consonant cluster (like ch or gr) --
    that consonant or cluster is moved to the end of the word followed by ay.
    eg -- name -> amenay
          chair -> airchay
Output shoul be:
    My name is AL SWEIGART and I am 4,000 years old.
    Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
'''
message = input("Enter the english message to change into pig latin: ")
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
