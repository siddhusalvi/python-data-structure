"""
8. Write a Python program to create set difference.
"""


def set_difference(set1, set2):
    new_set = set()
    for x in set1:
        if x not in set2:
            new_set.add(x)
    return new_set


set_1 = {2, 4, 5, 6, 11, 23, 45, 44, 31, 32, 33}
set_2 = {4, 6, 7, 8, 15, 48, 67, 84, 31, 32, 33}

print(set_difference(set_1, set_2))
