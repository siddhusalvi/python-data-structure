"""
6. Write a Python program to check whether an element exists within a tuple.
"""

def check_item(tuple,ele):
    for x in tuple:
        if x == ele:
            return True
    return False

tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
word = "mango"

print(check_item(tuple,word))


