def cancatinate(spam) :
    for i in spam:
        str = str + i[0: -2]
        str = str + "and" + i[-1]
