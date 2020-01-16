"""
6. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""


def convert_case(word):
    new_word = ""
    new_word2 = ""
    for x in word:
        if'a' <= x <= 'z':
            new_word += x
        else:
            new_word += chr(ord(x) + 32)
    print("Lower case :", new_word)
    for x in new_word:
        new_word2 += chr(ord(x)-32)
    print("Upper case :", new_word2)


word1 = input("enter any word : ")
convert_case(word1)
