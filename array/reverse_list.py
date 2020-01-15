"""
Write a Python program to reverse the order of the items in the array.
"""

def reverse_list(data):
    new_list = []
    for i in range(len(data),0,-1):
        new_list.append(i)
    return new_list
list =[1,2,3,4,5,6,7,8,9,10]
print(reverse_list(list))
