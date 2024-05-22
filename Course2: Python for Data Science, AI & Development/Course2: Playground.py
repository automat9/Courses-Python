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
import pandas as pd # this downloads pandas onto your computer, initiate in jupyter
DataFrame = pd.read_csv("my_fileWhatever_itCan_be.csv") # this loads data from my source and assigns it to a variable
