#! python3
#mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'greet': """Greeting from our company!"""}

import sys, pyperclip
if len(sys.argv) < 2 :
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()
# print(sys.argv[0])
# print(sys.argv[1])
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)