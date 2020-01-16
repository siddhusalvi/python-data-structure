"""
5. Write a Python program to remove an item from a set if it is present in the set.
"""


def remove_if_present(given_set, ele):
    if ele not in given_set:
        return -1
    given_set.discard(ele)
    return "item deleted "


days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
item = "Monday"
print(remove_if_present(days, item))
