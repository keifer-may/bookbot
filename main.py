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
    head = f'--- Begin report of {title} ---'
    tail = '--- End report ---'

    book = open(title, 'r')
    text = book.read()
    wordcount = wrdcnt(text)
    ##print(wordcount)
    charcount = cntchars(text)
    ##print(charcount)

    book.close()

    print(head)
    print(f'{wordcount} words found in the document\n')
    for char in charcount:
        print(f"The '{char}' character was found {charcount[char]} times")
    print(tail)

report('books/frankenstein.txt')
