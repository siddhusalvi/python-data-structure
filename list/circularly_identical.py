"""
14. Write a python program to check whether two lists are circularly identical.
"""


def are_circular_identical(given_list1, given_list2):
    new_list = []
    for i in range(2):
        for x in given_list1:
            new_list.append(x)
    for i in range(0, len(new_list) - len(given_list2)):
        counter = 0
        for j in range(len(given_list2)):
            if new_list[i + j] == given_list2[j]:
                counter += 1
        if counter == len(given_list2):
            return True
    return False


list1 = [4, 5, 1, 2, 3]
list2 = [1, 2, 3, 4, 5]
print(are_circular_identical(list1, list2))
