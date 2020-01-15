7. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
	Sample Words : red, white, black, red, green, black
	Expected Result : black, green, red, white,red
"""
def sort_words(str):
    list = []
    new_list = []
    start = 0
    count = 0
    for i in str:
        if i == ',':
            #print(str[start:count])
            temp = str[start:count]
            list.append(temp)
            start = count + 1
        count +=1
    temp = str[start:count]
    list.append(temp)
    while(len(list) != 0):
        flag = True
        for x in list:
            if flag:
                char = x[0]
                word = x
                flag = False
            elif x < char:
                char = x[0]
                word = x
        new_list.append(word)
        #print(word)
        list.remove(word)
    print(new_list)

str = input("enter words by , : ")
sort_words(str)
