"""
7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""


def print_unique_value(given_dict):  # funtion tu print unique value
    list1 = []
    for x, y in dict1.items():
        if y not in list1:
            list1.append(y)
    print(list1)


dict1 = {"V": "S001", "VI": "S002", "VIII": "S001", "IVI": "S005", "IIVII": "S005", "IIIVIII": "S009", "IIVIII": "S007"}
print(dict1)
print_unique_value(dict1)
