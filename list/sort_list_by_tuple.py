"""
5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""


def sorted_by_last(given_list):
    new_list = []
    while len(given_list) != 0:
        flag = True
        for x in given_list:
            if flag:
                minimum = x[-1]
                tuple1 = x
                flag = False
            elif minimum > x[-1]:
                minimum = x[-1]
                tuple1 = x
        new_list.append(tuple1)
        given_list.remove(tuple1)
    return (*new_list,)


list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted_by_last(list1))
