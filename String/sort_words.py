"""
7. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""


def sort_words(given_list):
    list = []
    new_list = []
    start = 0
    count = 0
    for i in given_list:
        if i == ',':
            #print(str[start:count])
            temp = given_list[start:count]
            list.append(temp)
            start = count + 1
        count +=1
    temp = given_list[start:count]
    list.append(temp)
    while len(list) != 0:
        flag = True
        for x in list:
            if flag:
                c = x[0]
                word = x
                flag = False
            elif x < c:
                c = x[0]
                word = x
        new_list.append(word)
        #print(word)
        list.remove(word)
    print(new_list)


words = input("enter words by , : ")
sort_words(words)

