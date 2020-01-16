"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""


def sort_dictionary_ascending(given_dict):
    flag = True
    new_list = []
    minimum = 0
    while len(given_dict) != 1:
        flag = True
        for x,y in given_dict.items():
            if flag:
                minimum = x
                flag = False
            elif minimum > x:
                minimum = x
        new_list.append(minimum)
        given_dict.pop(minimum)
    minimum, value = given_dict.popitem()
    new_list.append(minimum)
    print(new_list)


def sort_dictionary_descending(dict):
    flag = True
    list = []
    maximum = 0
    while len(dict) != 1:
        flag = True
        for x,y in dict.items():
            if flag:
                maximum = x
                flag = False
            elif maximum < x:
                maximum = x
        list.append(maximum)
        dict.pop(maximum)
    maximum, value = dict.popitem()
    list.append(maximum)
    print(list)


d = {1: 1, 3: 3, 4: 4, 2: 2, 5: 5}
sort_dictionary_descending(d)
d = {1: 1, 3: 3, 4: 4, 2: 2, 5: 5}
sort_dictionary_ascending(d)
