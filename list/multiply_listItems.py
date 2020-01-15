"""
2. Write a Python program to multiplies all the items in a list.
"""
def mul_listItems(list):#fuction to return sum of list
    ans = 1
    for x in list:
        ans *= x
    return ans

list = [1,2,3,4,5]
print(mul_listItems(list))
