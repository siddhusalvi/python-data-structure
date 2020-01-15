"""
7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

def print_unique_value(dict): #funtion tu print unique value
    list =[]
    for x,y in dict.items():
        if y not in list:
            list.append(y)
    print(list)


dict ={"V":"S001", "VI": "S002", "VIII": "S001", "IVI": "S005","IIVII":"S005", "IIIVIII":"S009","IIVIII":"S007"}
print(dict)
print_unique_value(dict)