"""
4. Write a Python program to remove the first occurrence of a specified element from an
array.
"""

def find_first_occurance(data,num):#function that returns first occurance index
    if num not in data:
        return -1
    new_list = []
    count = 0
    for i in data:
        if i == num:
            break
        new_list.append(i)
        count += 1
    for i in range (count+1,len(data)):
        new_list.append(data[i])
    print(new_list)

ele = 1
data =[1,2,3,4,5,6,7,8,1,2,3,4,2,1,3,1,2,4,2]
print(find_first_occurance(data,ele))
