Name = "Matt"
age = 22
print(f"My name is {name} and I'm {age} years old")

x = 53*32
y = -3*34.5
z = x+y
print(f"The sum of x and y is {z}")
#------------------------------------------------------
# String Operations
name = "Matt Pawlaczyk"
# In order to find index 7, type Name[7], the result will be "a"
print(name[0:4])
print(name[6:14])
print(name[::2])
print(name[0:7:2])
len("Matt Pawlaczyk") # = length of string
Statement = name + "is the best" # Combining strings
print(Statement)
3*"Matt Pawlaczyk" # prints 3 copies of the original string
# escape sequences are strings that are difficult to input, e.g. new like represented with \n, tab represented with \t
print("Matt is \n the best")
print("Matt is \t the best")
print("Matt is \\ the best")
# Upper/lower methods
A="I like cats"
B=A.upper()
print(B)
# Replace method
B=A.replace("cats","dogs")
# Find substrings
name.find("Paw")
# raw string "r" is used to treat string as raw text, meaning it inteprets \n, \t and other escape sequences as literal characters, e.g.:
file_destination = "C:\new_folder\file.txt"
print(file_destination) # escape sequence
raw_string = r"C:\new_folder\file.txt"
print(raw_string)
