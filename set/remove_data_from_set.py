"""
4. Write a Python program to remove item(s) from set
"""

days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days)
days.discard("Monday")
print(days)
days.remove("Thursday")
print(days)