def li_concat(spam) :
    string = ""
    if len(spam) == 0 :
        print("It is an empty list")
    elif len(spam) > 0 :
        string = string + spam[0]
        for i in range(1, (len(spam)-1)):
            string = string + ", " + spam[i]
        string = string + " and " + spam[-1]
    print(string)

li = ['apples', 'bananas', 'tofu', 'mary', 'cats', 'dogs', 'donkeys']
li_concat(li)
