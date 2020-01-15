"""
10. Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
"""
def get_true_count(list):
    count = 0
    for i in list:
        for x,y in i.items():
            if (x == "success" and y):
                count += 1
    return count
data= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
print(get_true_count(data))

