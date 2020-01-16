"""
10. Write a Python program to count occurrences of a substring in a string.
"""


def count_substring(given_str, substr):
    if substr not in given_str:
        return -1
    count = 0
    new_str = ""
    for x in given_str:
        if substr in new_str:
            count += 1
            new_str = x
        else:
            new_str += x
    if substr in new_str:
        count += 1
    print(count)


word = "issidhuisilansis"
print(word)
substring = "is"
count_substring(word,substring)