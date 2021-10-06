# Calculate the number of words and consonents in a given text
import re

n_dict = {}
# tot_vow = 0
# tot_con = 0
# vowels = ['a', 'e', 'i', 'o', 'u']
sentence = input("Enter a sentence to test no of vowels and consonents: ")
letters = re.findall("[a-zA-Z]", sentence)
# # print(letters)
#
# for l in letters :
#     if l in vowels:
#         tot_vow += 1
#     else:
#         tot_con = len(letters) - tot_vow
# print("total vowels are: ", tot_vow)
# print("total consonents are: ", tot_con)

for k, i in n_dict :
    n_dict[k] = i
    

print(n_dict)
