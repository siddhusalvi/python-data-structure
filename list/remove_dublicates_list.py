"""
6. Write a Python program to remove duplicates from a list.
"""
def remove_dublicates(list):#Function to remove dublicates
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    print(new_list)


List = [1,2,3,4,5,6,7,8,1,5,4,8,6,3]
remove_dublicates(List)