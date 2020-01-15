"""
11. Write a Python program to reverse a string.
"""
def reverse_string(str):
    reverse = ""
    for x in str:
        reverse = x +reverse
    return reverse
word = "machinelearning"
print(reverse_string(word))