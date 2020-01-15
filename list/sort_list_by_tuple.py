"""
5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
def sorted_by_last(list):
    new_list = []
    while(len(list)!=0):
        flag = True
        for x in list:
            if flag:
                min = x[-1]
                tuple = x
                flag = False
            elif min > x[-1]:
                min=x[-1]
                tuple = x
        new_list.append(tuple)
        list.remove(tuple)
    return (new_list)



list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted_by_last(list))



