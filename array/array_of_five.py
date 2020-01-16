"""
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""

arr = []
for i in range(0, 5):
    print("Enter a number for location ", i + 1, ": ")
    num = int(input())
    arr.append(num)
for i in range(0, len(arr)):
    num = arr[i]
    print(num)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
