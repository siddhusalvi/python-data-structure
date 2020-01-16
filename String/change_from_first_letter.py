"""
3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""


def find_replace_first(given_word1, given_word2):
    flag = True
    new_word = ""
    for x in given_word1:
        if flag:
            c = x
            flag = False
            new_word += x
        else:
            if c == x:
                new_word += given_word2
            else:
                new_word += x
    print(new_word)


word = "siddhesharunsalvissssssssssss"
c = '$'
find_replace_first(word, c)
