"""
12. Write a Python program to lowercase first n characters in a string.
"""


def lower_case_n(given_word, number):
    count = 0
    new_str = ""
    for x in given_word:
        if count < number and 'A' <= x <= 'Z':
            new_str += chr(ord(x)+32)
        else:
            new_str += x
        count += 1
    print(new_str)


word = "eXTERNALLY"
num = 3
lower_case_n(word,num)
