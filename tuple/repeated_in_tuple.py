"""
5. Write a Python program to find the repeated items of a tuple.
"""


def find_repeated_items(given_tuple):
    new_list = []
    for x in given_tuple:
        if x in new_list:
            print(x, "is repeated")
        else:
            new_list.append(x)
    print(new_list)


data = (1,2,3,4,5,6,7,8,9,2,3,4,5,5)
find_repeated_items(data)



