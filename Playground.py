Name = "Matt"
age = 22
print(f"My name is {Name} and I'm {age} years old")

x = 53*32
y = -3*34.5
z = x+y
print(f"The sum of x and y is {z}")
#------------------------------------------------------------------------------------------------------------
# String Operations
name = "Matt Pawlaczyk"
# In order to find index 7, type Name[7], the result will be "a"
print(name[7])
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
print(B)
# Find substrings
print(name.find("Paw"))
# raw string "r" is used to treat string as raw text, meaning it inteprets \n, \t and other escape sequences as literal characters, e.g.:
file_destination = "C:\new_folder\file.txt"
print(file_destination) # escape sequence
raw_string = r"C:\new_folder\file.txt"
print(raw_string)
#------------------------------------------------------------------------------------------------------------
# Tuples and lists
Ratings = (10,9,4,7,1,8,2,3)
print(Ratings)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)
List = ["Matt", 9.12, 2002]
print(List)
# Unlike tuples, lists are mutable, meaning they can be changed - e.g. extended using L.extend(["Bournemouth",2024])
print(List[0]) # is a way of finding elements using indices
List.append(["Bournemouth",2024]) # This will extend the list but will only add 1 new index ["Bournemouth",2024], instead of adding both elements separately
print(List)
say_what=('say','what','you','will')
print(say_what[-1])
A=(1,2,3,4,5)
print(A[1:4]) # elements from index 1 to 3 (element 1 = index 0, element 4 = index 3)
# [:3] means from the beginning up to index 2
# [2:] from index 2 to the end
# [::2] every second element
B=[1,2,[3,'a'],[4,'b']]
print(B[3][1]) # FIND EXPLANATION (ask chatgpt)
[1,2,3]+[1,1,1]
A=[1]
A.append([2,3,4,5])
print(A)
len(A) # counts the length of the list

