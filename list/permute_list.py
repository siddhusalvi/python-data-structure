"""
11. Write a Python program to generate all permutations of a list in Python.
"""

def list_permute(list,start,end):
    if start == end:
        print(list)
    else:
        for i in range(start,end+1):
            list[start] ,list[i] = list[i],list[start]
            list_permute(list,start+1,end)
            list[start], list[i] = list[i], list[start]

list = [1,2,3,4]

list_permute(list,0,len(list)-1)