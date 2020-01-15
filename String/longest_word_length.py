"""
5. Write a Python function that takes a list of words and returns the length of the longest one.
"""
def get_max_len(words):
    maxlen = 0
    for word in words:
        count  = 0
        for letter in word:
            count += 1
        if count > maxlen:
            maxlen = count
    return maxlen

words = ['a','abc','abcd','abcde','abcdefg','abcdefrg']
print(get_max_len(words))