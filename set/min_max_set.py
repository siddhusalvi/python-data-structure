"""
	12. Write a Python program to find maximum and the minimum value in a set.
"""
def set_min(set): #function that returns min value in set
    flag = True
    for x in set:
        if flag:
            min = x
            flag = False
        elif min>x:
            min = x
    return min

def set_max(set): #function that returns max value in set
    flag = True
    for x in set:
        if flag:
            max = x
            flag = False
        elif max < x:
            max = x
    return max

set = {1,2,3,4,5,6,7,8,9}
print(set_min(set))
print(set_max(set))