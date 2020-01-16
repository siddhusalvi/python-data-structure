"""
8. Write a Python program to remove an item from a tuple.
"""


def remove_from_tuple(given_tuple, ele):
    new_list = []
    if ele not in given_tuple:
        return -1
    flag = True
    for x in given_tuple:
        if flag and x == ele:
            print(x)
            flag = False
        else:
            new_list.append(x)
    return(*new_list,)


tuple1 = "w", "r", "s", "o", "u", "r", "c", "e"
ele = 'e'
tuple1 = remove_from_tuple(tuple1, ele)
print(tuple1)
