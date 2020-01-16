"""
12. Write a Python program to get the difference between the two lists.
"""


def list_difference(list1, list2):
    new_list = []
    for x in list1:
        if x not in list2:
            new_list.append(x)
    return new_list


li1 = [1, 2, 3, 4, 5, 6, 7, 8]
li2 = [1, 2, 3, 4]
print(list_difference(li1, li2))
