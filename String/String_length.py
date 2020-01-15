"""
	1. Write a Python program to calculate the length of a string.
"""
def count_length(str):
    count = 0
    for i in str:
        count += 1
    return count

print(count_length("siddhesh"))