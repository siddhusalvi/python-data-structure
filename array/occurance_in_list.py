"""
3. Write a Python program to get the number of occurrences of a specified element in an
array.
"""
def get_occurance(data ,num): #function to get occurance
    count = 0
    for i in data:
        if i is num:
            count += 1
    return count
    

data = [1,2,3,4,5,6,7,8,1,2,3,2,1,2,1,21,1]
num = 1
print(get_occurance(data,num))
