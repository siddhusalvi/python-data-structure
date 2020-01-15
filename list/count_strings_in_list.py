"""
4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2
"""

def count_string(list):
    count = 0
    for x in list:
        if len(x)>1 and x[0] ==x[len(x)-1]:
            count += 1
    return count



List = ['abc', 'xyz', 'aba', '1221','aba','moram']
print(count_string(List))
