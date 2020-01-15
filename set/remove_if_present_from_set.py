"""
5. Write a Python program to remove an item from a set if it is present in the set.
"""

def remove_if_present(set,item):
    if item not in set:
        return -1
    set.discard(item)
    return "item deleted "

days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
item = "Monday"
print(remove_if_present(days,item))
