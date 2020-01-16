"""
5. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def create_power_dictionary(number):  # function to create dictionary of numbers and powers
    dict1 = {}
    for i in range(1, number + 1):
        number = i
        power = number * number
        key = {number: power}
        dict1.update(key)
    print(dict1)


num = int(input("Enter a number to create dictionary : "))
create_power_dictionary(num)
