"""
8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""
def get_count_of_letters(word):#function that return dictionary from string
    dict = {}
    for x in word:
        count = 0
        for y in word:
            if x == y :
                count +=1
        record = {x:count}
        dict.update(record)
    return dict

word = "siddhesh"
print(get_count_of_letters(word))
