"""
11. Write a Python program to reverse a string.
"""


def reverse_string(given_word):
    reverse = ""
    for x in given_word:
        reverse = x + reverse
    return reverse


word = "machinelearning"
print(reverse_string(word))
