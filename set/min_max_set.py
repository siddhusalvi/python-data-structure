"""
12. Write a Python program to find maximum and the minimum value in a set.
"""


def set_min(given_set):  # function that returns min value in set
    flag = True
    for x in given_set:
        if flag:
            minimum = x
            flag = False
        elif minimum > x:
            minimum = x
    return minimum


def set_max(given_set):  # function that returns max value in set
    flag = True
    for x in given_set:
        if flag:
            maximum = x
            flag = False
        elif maximum < x:
            maximum = x
    return maximum


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_min(set1))
print(set_max(set1))
