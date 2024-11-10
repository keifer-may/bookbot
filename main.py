import functools

def wrdcnt(text):
    count = len(text.split())
    return count

def cntchars(text):
    lower = text.lower()
    lst = [x for x in {x for x in list(lower)}]
    set = list(filter(lambda x: x.isalpha(),lst))
    mydict = {x:lower.count(x) for x in set}
    mydict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
    return mydict

def report(title):
    pass

with open('books/frankenstein.txt', 'r') as book2:
    text = book2.read()
    wordcount = wrdcnt(text)
    print(wordcount)
    charcount = cntchars(text)
    print(charcount)
