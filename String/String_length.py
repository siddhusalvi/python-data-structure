"""
1. Write a Python program to calculate the length of a string.
"""


def count_length(given_word):
    count = 0
    for i in given_word:
        count += 1
    return count

print(count_length("siddhesh"))
