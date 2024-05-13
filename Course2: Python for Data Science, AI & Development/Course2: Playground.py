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
Statement = name + "is the best" # combining strings
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
# Raw string "r" is used to treat string as raw text, meaning it inteprets \n, \t and other escape sequences as literal characters, e.g.:
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
# Unlike tuples, lists are mutable, meaning the values can be changed after being created - e.g. extended using L.extend(["Bournemouth",2024])
print(List[0]) # is a way of finding elements using indices
List.append(["Bournemouth",2024]) # this will extend the list but will only add 1 new index ["Bournemouth",2024], instead of adding both elements separately
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
#------------------------------------------------------------------------------------------------------------
# Dictionaries
DictionaryA = {"Key1":1, "Key2":2, "Key3":3}
print(DictionaryA)
DictionaryA["Key1"] # will revtrive the value of Key1
DictionaryA.keys() # will give all the keys in dictionary
DictionaryA.values() # same but with values
DictionaryA["Key4"] = "4" # this will app Key4 to the dictionary
del(DictionaryA["Key4"]) # this will delete Key4
"Key4" in DictionaryA # verifies if Key4 is in dictionary - True or False
# Lab excercise
inventory = {}
# Create first variable
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_release = 2020
# Add first variable to the dictionary
inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_release"]= ProductNo1_release
# Second variable
ProductNo2 = "Laptop"
ProductNo2_quantity= 10
ProductNo2_price = 50000
ProductNo2_release= 2023
# Add to the dictionary
inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_release"]=ProductNo2_release
# Show the dictionary, check if release year is in the inventory, and then delease release year for both variables
print(inventory)
"ProductNo1_release" in inventory
del(inventory["ProductNo1_release"])
del(inventory["ProductNo2_release"])
# Syntax to extrack the keys as a list
list(dict.keys())
#------------------------------------------------------------------------------------------------------------
# Sets
SetFruit = {"apple", "orange", "passionfruit", "pineapple", "cranberry", "tomatoe", "apple", "orange"} # Duplicates apple and orange will not be printed
set(Ratings) # converts list into sets
SetFruit.add("another fruit")
SetFruit.remove("another fruit")
"apple" in SetFruit
SetVeg = {"potatoe", "carrot", "salad", "onions", "tomatoe"}
SetFruitAndVeg = SetFruit & SetVeg # finds intersection of both
print(SetFruitAndVeg) # prints intersection of both sets
SetFruit.union(SetVeg) # prints union of both sets
SetVeg.issubset(SetFruit) # contained in the set being referred to
SetVeg.issuperset(SetFruit) # contains the set being reffered to
SetFruitAndVeg.issubset(SetFruit)
SetFruit.difference(SetVeg) # shows all elements in SetFruit
#------------------------------------------------------------------------------------------------------------
# Conditions and Branching
A=6 # assigning value to variable
A==7 # result = False because not equal
A>3 # true because it is greater than 6 
A>=6 # greater than or equal to 6
A!=6 # not equal to 6 (False because it is)
# Comparing strings is also possible, also using ! if both strings are different
# If statements
age1 = 19
if(age1>18):
    print("You're an adult (not really)") # runs only condition is true
print("This is generated regardless of whether if statement is true or false")
age2 = 19
if(age2>18):
  print("This will generate if condition is true")
  elif(age2==18): # this == is very important, only one = will give an error because you want to compare 2 values
    print("This will generate if the first condition is false but this one is true") # there can be multiple elifs e.g. ==19,==20
else:
  print("This will generate if both conditions are false")
print("This will generate regardless - this line is unnecessary")
# OR & AND logic operators
album_year = 1990
if(album_year<1980) or (album_year>1989):
  print("The Album was made in the 70s or 90s")
else:
  print("The Album was made in the 1980s")
album2_year = 1983
if(album2_year>1979) and (album2_year<1990):
  print("This album was made in the 80s")
ageMatt = 22
if ageMatt == 22: # [pay attention to == and : at the end]
    print("You are 22 years old.")
#------------------------------------------------------------------------------------------------------------
# For Loops
for number in range(1,11):
    print(number) # best suited for sequences where the length is known
# another example
fruits = ["apple", "orange", "grapefruit", "pomegranate", "cranberry"]
N = len(fruits) # code is executed N times
for element in range(N): # each time the value of element is increased by 1 for every execution, so that element=0 => print(fruits[0]) => print("apple") and so on
    print(fruits[element]) # that element thingy here and above can be named as anything, "i", "yolo", "x" etc, it basically means index e.g. first element in the list is 0
# this code will change the elements in the list
squares = ['red', 'yellow', 'green', 'purple', 'blue'] # original list
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i]) # will print "Before square 0 is red" i=index, squares[i]=name of index in list
    squares[i] = 'white' # this changes the definition of squares[i] from red, yellow, green etc to white
    print("After square ", i, 'is',  squares[i]) # exactly the same formula except squares[i] now has a new definition
# this code will print both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)
# try to replace value of print() from i to Genres and see what happens
Genres = ["Rock", "R&B", "Soundtrack", "R&B", "Soul", "Pop"]
for i in Genres:
    print(i)
# 2 multiplication tables
print("Multiplication table of 6: ")
for i in range (10):
    print("6*", i, "=", 6*i)
print("Multiplication table of 7: ")
for i in range (10):
    print("7*", i, "=", 7*i)
# some more basic for loops
for x in range(0, 3):
    print(x)
for x in ['A', 'B', 'C']:
    print(x + 'A')
for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)
    
# While Loops
count = 1
while count <= 10:
    print(count)
    count += 1 # length is unknown, repeating the loop as long as condition is true (make sure the loop can end)
#another example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")
# taken from LAB - study this example --- while loop to display values of the rating of an album, exit loop if score < 6
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i]  
# This will create a new list with animals whose names are made of 7 letter
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
SevenletterAnimals=[] 
i = 0
while(i<len(Animals)):
      j=Animals[i]
      if(len(j)==7):
         SevenletterAnimals.append(j)
      i = i +1
print(SevenletterAnimals)
#------------------------------------------------------------------------------------------------------------
# Functions




