"""
8. Write a Python program to remove an item from a tuple.
"""
def remove_from_tuple(tuple,ele):
    new_list = []
    if ele not in tuple:
        return -1
    flag = True
    for x in tuple:
        if flag and x == ele:
            print(x)
            flag = False
        else:
            new_list.append(x)
    return(*new_list,)
tuple = "w","r", "s", "o", "u", "r", "c", "e"
ele = 'e'
tuple =remove_from_tuple(tuple,ele)
print(tuple)