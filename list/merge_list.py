"""
13. Write a Python program to append a list to the second list.
"""
def merge_list(li2,li1):#function to merge two lists
    for x in li1:
        li2.append(x)
    return li2

li1 = [1,2,3,4,5,6,7,8]
li2 = [1,2,3,4]
print(merge_list(li2,li1))