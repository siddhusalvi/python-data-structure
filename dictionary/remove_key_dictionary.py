"""
6. Write a Python program to remove a key from a dictionary.
"""
def remove_key(dict,key):
    if key in dict:
        del dict[key]
        print("key removed current dictionary :c")
        print(dict)
    else:
        print("Key not found!")

dict = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary",dict)
key=input("Enter the key to delete:")
remove_key(dict,key)
