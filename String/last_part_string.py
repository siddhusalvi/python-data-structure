"""
8. Write a Python program to get the last part of a string before a specified character.
	https://www.w3resource.com/python-exercises
	https://www.w3resource.com/python
"""
def string_before(str,char):
    if char not in str:
        return -1
    before_part = ""
    for x in str:
        if x == char:
            break
        before_part +=x
    return before_part

word = "https://www.w3resource.com/python-exercises"
char = '-'
print(string_before(word,char))