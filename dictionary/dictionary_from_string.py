"""
8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""


def get_count_of_letters(given_word):  # function that return dictionary from string
    dict1 = {}
    for x in given_word:
        count = 0
        for y in given_word:
            if x == y:
                count += 1
        record = {x: count}
        dict1.update(record)
    return dict1


word = "siddhesh"
print(get_count_of_letters(word))
