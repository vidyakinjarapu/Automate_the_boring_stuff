#Anagram eg : LISTEN --> SILENT  === Same letters change the place
word1 = input("Enter a word : ")
word2 = input("Enter the anagram of the word: ")
li1 = []
li2 = []
for i in word1 :
    li1.append(i)
    li1.sort()
for i in word2 :
    li2.append(i)
    li2.sort()

if li1 == li2:
    print("It is an anagram")
else:
    print("It's not an anagram")
