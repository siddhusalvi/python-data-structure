"""
4. Write a Python program to remove the first occurrence of a specified element from an
array.
"""


def find_first_occur(list1, num):  # function that returns first occurance index
    if num not in list1:
        return -1
    new_list = []
    count = 0
    for i in list1:
        if i == num:
            break
        new_list.append(i)
        count += 1
    for i in range(count + 1, len(list1)):
        new_list.append(list1[i])
    print(new_list)


ele = 1
data = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 2, 1, 3, 1, 2, 4, 2]
print(find_first_occur(data, ele))
