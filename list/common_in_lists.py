"""
9. Write a Python function that takes two lists and returns True if they have at least one common member.
"""
def check_common_in_list(list1,list2):#fuction return true if atlest one element is common in both list
    for x in list1:
        if x in list2:
            return True
    return False

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(check_common_in_list(list1,list2))