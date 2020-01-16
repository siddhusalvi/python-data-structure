"""
10. Write a Python program to reverse a tuple.
"""


def reverse_tuple(given_tuple):
    new_tup = ()
    for k in reversed(given_tuple):
        new_tup = new_tup + (k,)
    return (new_tup)


tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(reverse_tuple(tuple1))
