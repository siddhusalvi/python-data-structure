"""
10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""


def remove_items(given_list, indices):
    if max(indices) > len(given_list) - 1:
        return "invalid input"
    else:
        while len(indices) != 0:
            maximum = max(indices)
            given_list.pop(maximum)
            indices.remove(maximum)
        return given_list


List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices = [0, 4, 5]
print(remove_items(List, indices))
