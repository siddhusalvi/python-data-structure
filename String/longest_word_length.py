"""
5. Write a Python function that takes a list of words and returns the length of the longest one.
"""


def get_max_len(given_words):
    maximum_len = 0
    for word in given_words:
        count = 0
        for letter in word:
            count += 1
        if count > maximum_len:
            maximum_len = count
    return maximum_len


words = ['a', 'abc', 'abcd', 'abcde', 'abcdefg', 'abcdefrg']
print(get_max_len(words))
