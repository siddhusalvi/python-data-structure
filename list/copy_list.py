"""
	7. Write a Python program to clone or copy a list.
"""
def clone_list(list):
    new_list = []
    for x in list:
        new_list.append(x)
    return new_list

List = [1,2,3,4,5,6,7,8,1,5,4,8,6,3]
print(clone_list(List))