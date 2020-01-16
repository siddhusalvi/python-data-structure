"""
2. Write a Python script to add a key to a dictionary.
"""

dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
number = 4
ans = "d"
record = {number: ans}
dict1.update(record)
print(dict1)
