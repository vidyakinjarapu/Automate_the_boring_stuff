'''
message = "hello good morning!"
count = {}

for character in message :
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count)
'''
import pprint
message = "Hello good morning"
count = {}
for char in message :
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1
# pretty printing of the dictionaries using pprint library
print(pprint.pformat(count))
