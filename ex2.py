from xmlrpc.client import boolean


age = input("enter your age:")
print(type(age))
age = int(age)
print(type(age))
age=boolean(age)
print(type(age))
