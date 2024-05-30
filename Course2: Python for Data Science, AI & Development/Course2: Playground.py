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
def f(a): # input parameter "a"
    b=(a+4)*9; # function defines another variable using the given parameter
    return b # output
f(9) # input returns output

def f2(a, b): # example with multiple parameters
    c=a*b
    return c
f2(4,2) # can also do floats e.g. f2(53.234,43.21)

def f(a):
    """
    this explains what the hell is going on
    """
    # rest of code goes in here
help(f) # this will explain what function f does by providing description from the documentation strings

def thisFunction_doesNot_do_anything():
    pass # pass is used as a placeholder statement when we want to create a new function, but not specify any functionality yet, pass is mandatory to ensure the code is syntactically correct
#------ more complex function that adds/removes elements from a list
moja_lista = [] # this initial list will work as the data structure for the rest of this function
def dodaj_element(data_structure, element): # data_structure is the list to which I want to add elements, element is what I want to add to the list
    data_structure.append(element) # assigning functionality to "dodaj_element" - adds elements provided
def odejmij_element(data_structure, element): 
    if element in data_structure: # checks if element you want to remove is in the data set
        data_structure.remove(element) # assigning functionality
    else:
        print(f"{element} nie istnieje w zbiorze") # in case element is not in the set
dodaj_element(moja_lista, 19)
dodaj_element(moja_lista, 22)
dodaj_element(moja_lista, 24)
print("Moja lista to: ", moja_lista)
odejmij_element(moja_lista, 24)
print("Moja nowa lista to: ", moja_lista)
odejmij_element(moja_lista, 2245)
print("Kurde, nie mamy takiej liczby :(")
#------ example of a function that uses if/else statements
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"   
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

#------------------------------------------------------------------------------------------------------------
# Exception Handling
try:
    a = [1, 2, 3]
    a[10] # index error, list only has 3 indices
except:
    print("lol what did you think was gonna happen dumbass")
#------ divide b given by the used by a
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("Can't divide by 0") # this will only occur if b = 0
except ValueError:
    print("You need to provide a number")
except: # general except statement in case anything else happens 
    print("Something went wrong") 
else: # if no exceptions
    print("success a=", a)
finally: # will be executed at the end of the try except no matter what
    print("Processing complete")
#------ divide numerator by denominator, if 0 then return cannot divide by zero
def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator))
#------------------------------------------------------------------------------------------------------------
# Objects & Classes
# Creating a class and objects
class Car:
    max_speed = 120  # # Class attribute (shared by all instances, speed in km/h)
    def __init__(self, make, model, color, speed=0): # init is a constructor method (initialises instance attributes)
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0
    def accelerate(self, acceleration): # Method for accelerating the car
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    def get_speed(self): # Method to get the current speed of the car
        return self.speed
# Creating 2 objects of the car class
car1 = Car("Ford", "Fiesta", "Red")
car2 = Car("Volkswagen", "Golf", "Blue")
car1.accelerate(70) # the dot notaion means "to apply the method to the object", in this case to apply acceleration of 70 to car1
car2.accelerate(200)
# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.") # This will show 120km/h because he max speed is 120 and acelerating by 200 units will result in max speed
# Drawing circles using a library:
class Circle:
    # Constructor
    def __init__(self, radius=3, color='blue'): # american english spelling due to the library containing american spelling
        self.radius = radius
        self.color = color 
    # Method for adding radious
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    # Method for drawing circle
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 
InitialCircle = Circle() # default circle with the radious of 3 and colour blue
InitialCircle.drawCircle()
RedCircle = Circle(22, "red") # custom circles
RedCircle.drawCircle()
BlackCircle = Circle(25,"black")
BlackCircle.drawCircle()

# Now the same but rectangles
class Rectangle:
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
InitialRectangle = Rectangle()
InitialRectangle.drawRectangle()
MyCustomRectangle = Rectangle(234, 943,"g") # g can be used instead of green
MyCustomRectangle.drawRectangle()

# Creating another Car class, adding "assign capacity" and "show properties" methods
class Car:
    Colour = "White"
    def __init__(self, MaxSpeed, Mileage):
        self.MaxSpeed = MaxSpeed
        self.Mileage = Mileage
        self.Capacity = None
        
    def AssignCapacity(self, Capacity):
        self.Capacity = Capacity
        
    def ShowProperties(self):
        print("Properties of the Car: ");
        print("Max Speed: ", self.MaxSpeed);
        print("Mileage: ", self.Mileage);
        print("Capacity: ", self.Capacity);
        print("Colour: ", self.Colour)
        
Car1 = Car(200, 20)
Car1.AssignCapacity(5)
Car1.ShowProperties()
Car2 = Car(180, 25)
Car2.AssignCapacity(4)
Car2.ShowProperties()
#------------------------------------------------------------------------------------------------------------
# Text Analysis - Process of extracting meaningful info and insights from textual data, aka text mining/analytics
# 3 tasks: a) convert all the text to lowercase b) find frequency of each word c) track the frequency of a particular word
# 1) Define a string
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
# 2) Define the class and its attributes
class TextAnalyser:
    def __init__(self, text):
# 3) Implement a code to format the text in lowercase and remove punctuation       
        formattedText = text.replace(".","").replace("!", "").replace("?", "").replace(",", "") # remove punctuation
        formattedText = formattedText.lower() # make text lowercase
        self.fmtText = formattedText
# 4) Code to count the frequency of unique words   
    def freqAll(self):
        wordList = self.fmtText.split(" ") # spliting text into words
        freqMap = {} # creating dictionary
        for word in set(wordList): 
            freqMap[word] = wordList.count(word)
        return freqMap 
# 5) Code to count the frequency of a specific word
    def freq0f(self,word):
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
analysed = TextAnalyser(givenstring) # instance of TextAnalyser class
print("Formatted Text: ", analysed.fmtText) # converts data into lowercase
freqMap = analysed.freqAll() # counts frequency of all unique words
print(freqMap)
word = "lorem" # counts frequency of a specific word
frequency = analysed.freq0f(word)
print("The word", word, "appears", frequency, "times.")
#------------------------------------------------------------------------------------------------------------
# Reading a file with Open()
# Opening the file in read (r) mode
file =open("/desktop/file.txt", "r") # 2 parameters, file path & file name + mode (the others being w for writing and a for appending)
with open("file.txt", "r") as file: # best practice, ensures proper closure of files when indented blocks are completed - no need to call close()
    File = "file.txt"
    Example = open(File, "r")
    FileContent = Example.read()
    print(FileContent) # or something like that
# All steps in order + bonus commands
#1) Import a file, if working locally you need a path i.e. look above
#2) file.name = returns the name of the file, file.mode = returns the mode e.g. r or w, file.read() = reads raw text, print(x) where x is a variable to which the file is assigned = returns formatted text, type(x) = returns string or something, file.close() = you guessed it, file.closed = verifies if file closed
#3) read first 4 characters (including spaces)
 with open("file.txt", "r") as File:
     print(File.read(4)) 
#4) read multiple amounts of characters:
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4)) # this will start from where the first line ended (4th character)
    print(file1.read(7))
    print(file1.read(15))
#5) if you want to read one line at a time (if your text file has multiple \n lines) do:
with open(example1, "r") as file1:
    print(file1.readline())
#6) readline allows us to specify how many characters we wanna read, but it can only read one line, so if line 1 has 20 characters and we want to read 5000, it'll only print off the 20 that are in the line:
print(file1.readline(20)) # does not read past the end of line
print(file1.read(20)) # Returns the next 20 chars
#7) using a loop to iterate through the lines:
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
# result:
Iteration 0 :  This is line 1 
Iteration 1 :  This is line 2
Iteration 2 :  This is line 3
#------------------------------------------------------------------------------------------------------------
# Writing files with Open
with open("file.txt", "w") as file: # w instead of r this time, now we can write in the file
    file.write("This is line 1\n") # again, \n starts a new line
    file.write("This is line 2") 
    # closes notebook automatically thanks using with function
# This is how you can use loops to add multiple lines at the same time
Lines = ["This is line 1", "This is line 2", "This is line 3"]
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
# This is how you can append data to an existing file
new_data = "This is line C"
with open('Example2.txt', 'a') as file1: # a for append
    file1.write(new_data + "\n")
# Copying contents from one file to another
with open('source.txt', 'r') as source_file:
    with open('destination.txt', 'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
# Last excercise from lab is an interesting example, do have a look if you want a more complex code
#------------------------------------------------------------------------------------------------------------
# Panads
import pandas as pd # this downloads pandas onto your computer, initiate in jupyter, this HAS TO BE INITIATED before the rest of your pandas code
DataFrame = pd.read_csv("my_fileWhatever_itCan_be.csv") # this loads data from my source and assigns it to a variable - make sure to change it to an actual file path like \desktop\blablabla
#--- series
data = [10, 20, 30, 40, 50] # here we're creating a series, a single column with labels or indeces for each element
s = pd.Series(data) # assigning the series to a variable
print(s)
# You can access elements using 3 different ways:
print(s[2]) # accessing element with label 2
print(s.iloc[3]) # accessing element at position 3
print(s[1:4]) # accessing multiple elements from the range
#--- dataframes
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} # first we create a dictionary
df = pd.DataFrame(data) # assign it to a variable
print(df) # print the variable
# accessing stuff from dataframes:
print(df['Name']) # accessing the name column
print(df.iloc[2]) # access THIRD row by POSITION
print(df.loc[2]) # access third row by label
print(df[['Name', 'Age']]) # select specific columns
print(df[1:3]) # accessing specific rows
unique_dates = df['Age'].unique() # this will determine the unique elements in a column if many of them are the same
high_above_102 = df[df['Age'] > 25] # this will filter albums released after a certain year
df.to_csv('trading_data.csv', index=False) # saving a dataframe using to_csv method
#--- another example of creating a dataframe using a dictionary:
#Import pandas
import pandas as pd
#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#display the result df
df
# Retreiving a column and assigning it to a variable x
x = df[['ID']] # try other keys as well, like name, department
x
# Retreiving multiple columns and assigning them to another variable
z = df[['Department','Salary','ID']]
z
# To view the column as a series, just use one bracket
x = df['ID']
x
# And to check the type of x type:
type(x)
# loc() - label-based data selecting method, we need to pass the name or column that we want to select
loc[2,'ID']
# iloc() indexed-based selecting method, we need to pass an integer in the method to select specific row or column
iloc[2,3] # first row x then column y
# printing first five rows of the dataframe
df.head()
# Slicing the dataframe (accessing a small portion of it)
df.loc[0:2, "Name":"Department"]
# Changing existing indices from numbers to characters using a list
new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new # this will print same list different indices
# Accessing things using these new indices
df_new.loc['a', 'Department']
df_new.loc['a':'d', 'Salary']
#------------------------------------------------------------------------------------------------------------
# NumPy
import numpy as np # numpy is usually imported under the np alias
a = np.array([0,1,2,3,4,5,6])
a # creating a numpy array
a[4] # accessing 5th element via a square bracket (first being 0)
a[4] = 100 # changing the 5th element to 100, if you type c, you'll get an updated array
a[3:5] = 233, 653 # changing the fourth and fifth elements (the 5 is not included in the output-goes up to 4)
a[:4] # the missing first index is considered 0 in this case
a[4:] # from fifth till the length of array
a[1:7:2] # til element 7 skipping every other element
# Lists can be used to select more than one specific index
select_these = [0,3,5]
b = a[select]
b # indices 0,3,5 will be selected from array a
a[select] = 0901 # assigning the specified elements to a new value (elements 0,3 and 5 from array a will turn into 0901
a.size # gives the number of elements in the array
a.ndim # this represents the number of array dimensions, or the rank of array (will make more sence once we get to higher dimensions)
a.shape # tuple of integers indicating the size of the array in each dimension
# Statistical NumPy (how exciting)
mean = a.mean()
mean # you'll never believe what this does
a.std() # standard deviation
a.max() a.min() # biggest/smallest values
# arithmetic with 2 arrays
x = np.array([1,2,3])
y = np.array([4,5,6])
za = np.add(x,y) # result will be array([5,7,9)]
zb = np.subtract(x,y) # remember, using print(zb) will instead generate [], not array([])
zc = np.multiply(x,y)
zd = np.divide(x,y)
ze = np.dot(x,y) # not sure what this is tbh, google says it means applying one vector to another, the product is how much stronger we've made the original vector
# ok so basically ^^^ stuff does this:
# we know that x = [1,2,3] where 1 = x[0], 2 = x[1] and 3 = x[2], same with y, y[0] = 4, y[1] = 5 etc
# dot does = [(x[0] * y[0]) + (x[1] * y[1]) * (x[2] * y[2])]
# which gives [4 + 10 + 18] = 32 - THIS IS CALLED MATRIX MULTIPLICATION
g = np.array([7,8,9])
g + 1 # array([8,9,10])
np.pi # pi, the number, what did you think it would print you dumbo
np.linspace(-2,6,num=3) # (start,stop,num = int value, this will create an array from -2 to 6 with evenly spaced intervals within that range in this case 3 intervals)
# REMEMBER THAT THE ONLY REASON EVERY OPERATION HERE STARTS WITH np. IS BECAUSE WE IMPORTED NUMPY AS np, OTHERWISE ALL OF IT WOULD HAVE BEEN numpy.add, numpy.linspace etc)
# creating a loop to iterate through each element
for x in g:
    print(x) # if we just typed print(x) without the for x in g, we would get [7,8,9]

#---*Something Special*
import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
# now try :)
a = np.array([-1,1])
b = np.array([1,1.5])
Plotvec2(a,b)
#---
# Finding the even and odd numbers from arr1 and arr2
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)
#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)
#---
#------------------------------------------------------------------------------------------------------------
# 2D NumPy
# A = array([[11, 12, 13],
#           [21, 22, 23],
#           [31, 32, 33]]) 
# If you want to find out what's on the second row and third column, type A[1,2] - first which row (first being 0), then which column
# You can also do A[1][2] instead for the same result
# But if you want to obtain a range, do e.g. A[1][1:2] - meaning elements from second row, second to third elements
# If you want A[0:2,2], you,ll get first to second rows (yes, second, not third, even tho A[2] is third row), third column elements
#------------------------------------------------------------------------------------------------------------
# API - see projects
#------------------------------------------------------------------------------------------------------------
# REST APIs & HTTP Requests
import requests # a library that allows you to send HTTP/1.1 requests easily

# some other libraries that will be needed for os to work
import os 
from PIL import Image
from IPython.display import IFrame

url = "https://www.youtube.com/"
r = requests.get(url) # this is a get method that will retreive data from the server
r.status_code # 200 stands for OK
print(r.request.headers) # headers of the request, duh
print(r.request.body) # None, as there is no body for a get request

header = r.headers
print(r.headers) # this will allow you to view the HTTP response header, it will return a python ditionary of HTTP response headers
heaer["date"] # obtains the date the request was sent 
header["Content-Type"] # indicates the type of data
r.encoding # checks the encoding
r.text[0:100] # as Contant-Type is text/html, we can use the text attribute to display the HTML in the body, here we have first 100 characters

# now onto images
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=request.get(url) # get request
print(r.headers)
r.headers['Content-Type'] # surprise surprise - image/png
# now since images are response objects that contain the images as bytes-like object, we must save them using a file object, so let's first specify the file path and name:
path=os.path.join(os.getcwd(),'image.png')
# we save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path) # now we can view the image
#------------------------------------------------------------------------------------------------------------
# API examples -again, API is a piece of software that acts as an intermediary that allows 2 applications to talk to each other
# RandomUser - generates random users to be used as placeholders
!pip install randomuser
from randomuser import RandomUser
import pandas as pd
r = RandomUser() # creating a random user object, r
some_list = r.generate_users(5)
some_list # dayumm here you have a list of 5 randomly generated users
name = r.get_full_name() # now we want to give those 5 random users names and emails
for user in some_list:
    print(user.get_full_name(), " ", user.get_email()) # using a for loop to give names to the 5 random users
for user in some_list:
    print(user.get_picture()) # omg it can also generate pictures
# more comands for your convenience :)
get_cell()
get_city()
get_dob()
get_email()
get_first_name()
get_full_name()
get_gender()
get_id()
get_id_number()
get_id_type()
get_info()
get_last_name()
get_login_md5()
get_login_salt()
get_login_sha1()
get_login_sha256()
get_nat()
get_password()
get_phone()
get_picture()
get_postcode()
get_registered()
get_state()
get_street()
get_username()
get_zipcode()
def get_users(): # generating a table with information about the users
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)  

# Fruityvice - provides data for all kinds of fruit
import requests # using requests (accessing web info) to generate answers
import json
# we obtain the fruityvice API data using requests.get("url"), result is in a json format
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text) # retreiving results
pd.DataFrame(results) # converting the json data into pandas data frame
# the result is in a nested json format, the nutrition column contains multiple subcolumns, so let's normalise it:
df2 = pd.json_normalize(results)
df2 # voila
cherry = df2.loc[df2["name"] == 'Cherry'] # extracting specific info
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# Official Joke API
x = requests.get("https://official-joke-api.appspot.com/jokes/ten") # loading the data from the URL
result = json.loads(x.text) # retreiving results
result 
result_no_Type_or_ID = pd.DataFrame(result) # converting json data into pandas data frame
result_no_Type_or_ID.drop(columns=["type", "id"],inplace=True) # dropping type and id columns because we don't need em
result_no_Type_or_ID
#------------------------------------------------------------------------------------------------------------
# Web Scraping
# Beautiful Soup is a python library used for pulling data out of HTML and XML files, this is accomplished by representing the HTML as a set of objects with methods used to parse the HTML
!pip install html5lib # first let's download a few modules
!pip install bs4
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
#---Our example HTML---
%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
# store it in a variable
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib') # parsing the document by passing it into the BeautifulSoup constructor, this soup constructor represents the document as a nested data structure
print(soup.prettify()) # displaying the HTML in the nested structure
# Basically Beautiful Soup transforms complex HTML docs into complex trees of Python objects
TAGS IN WEB SCRAPING LAB
