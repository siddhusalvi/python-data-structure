"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""


def sort_dictionary_ascending(dict):
    flag = True
    list = []
    minx = 0
    while(len(dict)!=1):
        flag = True
        for x,y in dict.items():
            if flag:
                minx = x
                flag = False
            elif minx>x:
                minx =x;
        list.append(minx)
        dict.pop(minx)
    minx,value= dict.popitem()
    list.append(minx)
    print(list)


def sort_dictionary_descending(dict):
    flag = True
    list = []
    maxx = 0
    while(len(dict)!=1):
        flag = True
        for x,y in dict.items():
            if flag:
                maxx = x
                flag = False
            elif maxx < x:
                maxx = x
        list.append(maxx)
        dict.pop(maxx)
    maxx,value= dict.popitem()
    list.append(maxx)
    print(list)


d = {1: 1, 3: 3, 4: 4, 2: 2, 5: 5}
sort_dictionary_descending(d)
d = {1: 1, 3: 3, 4: 4, 2: 2, 5: 5}
sort_dictionary_ascending(d)
