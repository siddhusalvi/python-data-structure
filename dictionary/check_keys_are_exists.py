"""
12. Write a Python program to check multiple keys exists in a dictionary.
"""


def check_keys(given_dict, given_keys):
    for x, y in given_dict.items():
        if x in given_keys:
            print(x, "is present in dictionary")


dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
keys = [1, 5, 7, 3]
check_keys(dict1, keys)
