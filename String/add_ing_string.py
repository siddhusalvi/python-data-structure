"""
4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
	Sample String : 'abc'
	Expected Result : 'abcing'
	Sample String : 'string'
	Expected Result : 'stringly'
"""
def add_ing(str):
    count = 0
    for x in str:
        count += 1
    if count <3:
        return -1
    if str[count-3:] == 'ing':
        return str + 'ly'
    return str + "ing"
word1 = "abc"
word2 = "string"

print(add_ing("king"))
print(add_ing(word1))
print(add_ing(word2))