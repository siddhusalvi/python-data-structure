"""
11. Write a Python program to generate all permutations of a list in Python.
"""


def list_permute(given_list, start, end):
    if start == end:
        print(given_list)
    else:
        for i in range(start, end + 1):
            given_list[start], given_list[i] = given_list[i], given_list[start]
            list_permute(given_list, start + 1, end)
            given_list[start], given_list[i] = given_list[i], given_list[start]


list1 = [1, 2, 3, 4]
list_permute(list1, 0, len(list1) - 1)
