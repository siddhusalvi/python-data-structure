"""
9. Write a Python program to slice a tuple.
"""
tuple1 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1, 10, 11)

slice1 = tuple1[3:5]
print(slice1)

slice2 = tuple1[:len(tuple1)]
print(slice2)

slice3 = tuple1[2:]
print(slice3)

slice4 = tuple1[-8:-2]
print(slice4)

slice5 = tuple1[2:9:2]
print(slice5)

slice6 = tuple1[::4]
print(slice6)










