"""
4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""


def add_ing(given_word):
    count = 0
    for x in given_word:
        count += 1
    if count < 3:
        return -1
    if given_word[count - 3:] == 'ing':
        return given_word + 'ly'
    return given_word + "ing"


word1 = "abc"
word2 = "string"

print(add_ing("king"))
print(add_ing(word1))
print(add_ing(word2))