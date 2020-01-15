"""
13. Write a Python program to count number of items in a dictionary value that is a list.
"""
def count_list(dict):
    count = 0
    for i,j in dict.items():
        if isinstance(j,list):
            count += 1
    return count
d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],'B': 34,'C': 12,'D': [7, 8, 9, 6, 4]}
print(count_list(d))