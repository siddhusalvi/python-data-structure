"""
	9. Write a Python program to create a symmetric difference.
"""
def set_symmetric_difference(set1,set2):
    set3 = set1-set2
    set4 = set2-set1
    return set3.union(set4)

set1 = {2, 4, 5, 6, 11, 23, 45, 44, 31, 32, 33}
set2 = {4, 6, 7, 8, 15, 48, 67, 84, 31, 32, 33}
print(set_symmetric_difference(set1,set2))
