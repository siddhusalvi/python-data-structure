"""
2. Write a Python program to count the number of characters (character frequency) in a string.
	Sample String : google.com
	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
def count_char_occurance(word):
    dict = {}
    for x in word:
        count = 0
        for y in word:
            if x == y :
                count +=1
        record = {x:count}
        dict.update(record)
    return dict

word = "google.com"
print(count_char_occurance(word))
