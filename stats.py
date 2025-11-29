import functools

def get_num_words(text):
    count = len(text.split())
    return count


def count_chars(text):
    lower = text.lower()
    lst = [x for x in {x for x in list(lower)}]
    set = list(filter(lambda x: x.isalpha(),lst))
    mydict = {x:lower.count(x) for x in set}
    mydict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
    return mydict

