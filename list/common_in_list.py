"""
	15. Write a Python program to find common items from two lists.
"""

def list_intersection(list1,list2):
    new_list = []
    for x in list1:
        if x in list2:
            new_list.append(x)
    return new_list

li1 = [1,2,3,4,5,6,7,8]
li2 = [1,2,3,4]

print(list_intersection(li1,li2))