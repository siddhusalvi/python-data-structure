"""
8. Write a Python program to find the list of words that are longer than n from a given list of words.
"""


def check_word_length(given_list, given_lenth):
    count = 0
    for i in given_list:
        if len(i) > given_lenth:
            count += 1
    return count


Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
number = 6

print(check_word_length(Days, number))
