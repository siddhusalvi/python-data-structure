"""
9. Write a Python program to print a dictionary in table format.
"""


def dict_to_table(dict):  # function to print dictionary in tabular format
    output = "key\tvalue\n"
    for x, y in dict.items():
        output += str(x) + "\t" + str(y) + "\n"
    print(output)


dict1 = {1: [1, 2, 3, ], 2: [4, 5, 6, ], 3: [7, 8, 9], 4: [11, 21, 13]}
dict_to_table(dict1)
