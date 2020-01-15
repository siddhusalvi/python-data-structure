"""
	10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
	Expected Output : ['Green', 'White', 'Black']
"""
def remove_items(list,indices):
    if(max(indices)>len(list)-1):
        return  "invalid input"
    else:
        while(len(indices)!=0):
            maxin = max(indices)
            list.pop(maxin)
            indices.remove(maxin)
        return list

List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices = [0,4,5]
print(remove_items(List,indices))