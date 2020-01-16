"""
1. Write a Python program to sum all the items in a list.
"""


def total_of_list(given_list):  # fuction to return sum of list
    total = 0
    for x in given_list:
        total += x
    return total


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(total_of_list(list1))
