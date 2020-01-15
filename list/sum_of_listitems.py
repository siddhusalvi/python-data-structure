"""
1. Write a Python program to sum all the items in a list.
"""
def sum_of_listItems(list):#fuction to return sum of list
    sum = 0
    for x in list:
        sum += x
    return sum

list = [1,2,3,4,5,6,7,8,9,10]
print(sum_of_listItems(list))
