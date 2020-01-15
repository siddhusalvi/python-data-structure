"""
3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
	Sample String : 'restart'
	Expected Result : 'resta$t'
"""
def find_replace_first(str,str2):
    flag = True
    new_word = ""
    for x in str:
        if flag:
            char = x
            flag = False
            new_word += x
        else:
            if char == x:
                new_word += str2
            else:
                new_word +=x
    print(new_word)


word = "siddhesharunsalvissssssssssss"
char ='$'
find_replace_first(word,char)