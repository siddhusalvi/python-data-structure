"""
13. Write a Python program to append a list to the second list.
"""


def merge_list(given_list1, given_list2):  # function to merge two lists
    for x in given_list2:
        given_list1.append(x)
    return given_list1


li1 = [1, 2, 3, 4, 5, 6, 7, 8]
li2 = [1, 2, 3, 4]
print(merge_list(li2, li1))
