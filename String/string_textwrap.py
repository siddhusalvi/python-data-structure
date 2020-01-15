"""
	9. Write a Python program to display formatted text (width=50) as output.
"""

def print_format_text(str,width):
    count = 0
    new_str =""
    for x in str:
        if count % width == 0:
            new_str += '\n'
        new_str += x
        count +=1
    print(new_str)



big_string ="""The assignment statement (token '=', the equals sign). This operates differently than in traditional imperative programming languages, and this fundamental mechanism (including the nature of Python's version of variables) illuminates many other features of the language. Assignment in C, e.g., x = 2, translates to "typed variable name x receives a copy of numeric value 2". The (right-hand) value is copied into an allocated storage location for which the (left-hand) variable name is the symbolic address"""
print_format_text(big_string,50)