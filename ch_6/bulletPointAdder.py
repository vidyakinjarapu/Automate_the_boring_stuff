asdsd'''
get the text from the clipboard, add a star and space to the beginning of each
line, and then paste this new text to the clipboard.

1.Paste text from the clipboard.
2.Do something to it.
3.Copy the new text to the clipboard. '''

#!python
import pyperclip
text = pyperclip.paste()
# print(text)
#Code to add star and a space
lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    print (lines[i])

text = '\n'.join(lines)
pyperclip.copy(text)

# Lists of animals
# Lists of aquarium life
# Lists of biologists by authorabbreviation
# Lists of cultivars
