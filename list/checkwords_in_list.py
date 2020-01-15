"""
8. Write a Python program to find the list of words that are longer than n from a given list of words.
"""

def check_word_length(list,lenth):
    count = 0
    for i in list:
        if len(i)>lenth:
            count += 1
    return count

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
num  = 6

print(check_word_length(Days,num))
