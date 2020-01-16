"""
6. Write a Python program to check whether an element exists within a tuple.
"""


def check_item(given_tuple, ele):
    for x in given_tuple:
        if x == ele:
            return True
    return False


tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
word = "mango"

print(check_item(tuple1, word))
