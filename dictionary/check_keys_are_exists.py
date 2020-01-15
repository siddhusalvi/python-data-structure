"""
12. Write a Python program to check multiple keys exists in a dictionary.
"""
def check_keys(dict,keys):
    for x,y in dict.items():
        if x in keys:
            print(x,"is present in dictionary")

data = {1: 'a',  2: 'b',  3: 'c', 4: 'd'}
keys = [1,5,7,3]
check_keys(data,keys)
