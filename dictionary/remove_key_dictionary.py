"""
6. Write a Python program to remove a key from a dictionary.
"""


def remove_key(given_dict, key1):
    if key1 in given_dict:
        del given_dict[key1]
        print("key removed current dictionary :c")
        print(given_dict)
    else:
        print("Key not found!")


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Initial dictionary", dict1)
key = input("Enter the key to delete:")
remove_key(dict1, key)
