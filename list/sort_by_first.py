"""
16. Write a Python program to split a list based on first character of word.
"""


def list_by_chr(given_list):
    new_list = []
    for x in given_list:
        if x[0] not in new_list:
            new_list.append(x[0])
            for y in given_list:
                if x[0] == y[0]:
                    new_list.append(y)
    return new_list


words = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think', 'look', 'want', 'give',
         'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
print(list_by_chr(words))
