# integer e.g. 1,3,4,5  = int
# real number e.g. 1.4, 54.22, 9493,34555 = float
# string e.g. "Hello World" = str
# boolean = True(1)/False(0) = bool (upper case mandatory)
# iterating means going through elements one by one
# to find out what type of an expression you're dealing with, use type(), e.g. type(-12), type(3.14), type("hello world")
# use sys.float_info to find out about the specifics of floats for your runtime environment (smallest/largest number that can be represented with them)
# to convert an integer into a float, use float(), use type(float(2)) to convert and also check its type
# type(6/2) = float division, type(6//2) = result is rounded down to nearest integer (loss of data)
# float 3.99 won't be rounded up if converted into an integer, the result will be: 3
# Variables or constants (numbers) are called operands, and math symbols are called operators
# Tuples are an ordered sequence written as comma-separated elements within parentheses e.g. Ratings = (1,2,3,4,5)
# Another example: tuple1 = ("disco",10,1.2), if we type tuple1[0]: "disco, duple1[2]: 1.2
# First element in a list using index = L[0], but LAST = L[-1]
# Dictionaries use curly brackets {}, and have keys instead of indices and values instead of elements. The *key* difference is that the keys don't have to be integers
# Sets are a type of collection like lists, tuples, but unlike them, sets are unordered (no record of element position), furthermore, they act like sets in mathematics, they can have intersections and unions
# = is used for assignment (e.g. A = (1,2,3,4,5), whereas == is used for comparison (to check if A & B are equal, try print(sum(A)), print(sum(B)), != means "not equal to"
# Logic operators take boolean values and produce different boolean values e.g. turning True using not(True) into False, False into True using not(False) - other logics include also be OR & AND
# new statement under "if" will only be executed if there's an indent and the statements are true, otherwise the tasks will end
# else is used if none of the conitions are true before this else statement, else has no condition unlike if (e.g. if age > 18)
# Branching is basically that whole "if A = B do X, else Y" 
# 2 types of loops: for and while
# for = allows for repeated execution of a set of statements for each item in a sequence (e.g. elements in a list or numbers in range)
 # syntax for = for value in sequence:
 # use for when = you know the number of iterations in advance (e.g. how many elements in a list)
 # example = list of colours = ["green", "red", "orange"], to print all of the colours at the same time, write:
    # for colour in colours:
         # print(colour)
# while = allows for a task to run as long as a certain condition is true, e.g. keep changing colours until you land on green, then stop
 # syntax while = while >condition<: (indentation is crucial to indicate the scope of the loop)
 # use while when = you don't know the number of iterations or if you're waiting for a specific condition to be met
 # example = count = 1 (below) while count <=10: (below & indent) print(count) (below) count+=1 <--- this increases each output by 1, without it the loop will never stop (bad)
# range function: generates an ordered sequence that can be used in loops
# if one argument, e.g. range(14), it generates a sequence from 0 up to, but not including given number
# if two arguments, e.g. range(14,32), it generates a sequence from 14 up to, but not including the second argument
# example: for number in range(43) print(number)
# functions: reusable blocks of code that execute a certain functionality when it is called, used if you need to perform a function multiple times, no need to duplicate the same code, just use the defined function instead
# e.g. YourVariable=len(YourList) - determines length of list, YV=sum(YL) - total of all elements, YV = sorted (YL) lowest to highest
# to define a function start with def, decriptive name of function e.g. add1
# make sure to document what each function does, using triple """description""" or #
# in many cases a function does not have a return statement, in this case the function returns nothing, e.g. function def MP(): print("Mateusz Pawlaczyk") will only print the string if MP() is called
# bult-in functions include: len():, sum();, max():, min():
# keep in mind that variables can be both global (defined outside functions, accessible everywhere), and local (only usable within the functions they were defined in)
# The whole process is: 1) def "function name"() 2) input parameters or arguments in the parentheses 3) can also define parameters inside these parentheses 4) there's a body within every function starting with : and is indented 5) you can place documentation before the body 5) return exists a function, optionally passing back a value
# Exception handling = alert when something unexpected happens while running a program.
# Errors are big, computer or system related, they prevent the program stop working completly, exceptions are controlled issues that are less severe and are a result of problematic code execution
# examples of exception classes: ArithmeticError, IOError, ValueError (e.g. trying to convert a non-numeric string to an integer)
# Process:
try: # code that may result in an exception is contained in the try block
    result = 10 / 0
except ZeroDivisionError: # if an exception occurs, the code directly jumps to this except block
    print("Error: Cannot divide by zero") # defining how we want this to be handled, e.g. message or alternative action
print("outside of try and except block") # after the except block, the program continues executing the remaining code
# Classes: blueprints or templetes for creating objects. Define structure and behaviour that their objects will have (e.g. class = car, attributes = colour, speed, methods (functions) = accelerate)
# Objects: fundamental units in python, represent real-world entity or concept, can be tangible (e.g. car), or abstract (student grade)
     # 2 characteristics: state (attributes that describe objects e.g. colour or speed), behaviour (actions that object can perform i.e. functions)
# Summary:
# Class = blueprint that contains attributes and methods (e.g. colour, size, weight, but also creating methods like change size)
# Methods = ways to interact with objects from a specific class (e.g. accelerating a car)
# Open() is used to read the text files (".txt" files), it involved extracting and processing the data stored within them.
# Dependencies or libraries are prewritten codes to help solve problems - e.g. pandas is a popular library for data analysis
# Pandas is open source and data manipulation and analysis library, great for structured data, making it fundamental for analysts
# Used to handle various formats, like tabular data, time series data and more - essential of the data processing workflow
# 2 primary data structures offered: DataFrame and Series, first is a table that can be manipulated, second is a single column or row of data
# Makes it easy to read data from CSV, Excel, SQL databases and more, can also export data in these formats
# Can combine multiple DataFrames using methods like merge and join (similar to SQL), to create more complex datasets
# Excellent indexing makes accessing specific rows of data very quick
# Custom data structures means you're not limited to tables and series
# SERIES attributes and methods to help you manipulate and analyse data using pandas:
  # values: Returns the Series data as a NumPy array.
  # index: Returns the index (labels) of the Series.
  # shape: Returns a tuple representing the dimensions of the Series.
  # size: Returns the number of elements in the Series.
  # mean(), sum(), min(), max(): Calculate summary statistics of the data.
  # unique(), nunique(): Get unique values or the number of unique values.
  # sort_values(), sort_index(): Sort the Series by values or index labels.
  # isnull(), notnull(): Check for missing (NaN) or non-missing values.
  # apply(): Apply a custom function to each element of the Series.
# DataFrame attributes and methods:
  # shape: Returns the dimensions (number of rows and columns) of the DataFrame.
  # info(): Provides a summary of the DataFrame, including data types and non-null counts.
  # describe(): Generates summary statistics for numerical columns.
  # head(), tail(): Displays the first or last n rows of the DataFrame.
  # mean(), sum(), min(), max(): Calculate summary statistics for columns.
  # sort_values(): Sort the DataFrame by one or more columns.
  # groupby(): Group data based on specific columns for aggregation.
  # fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
  # apply(): Apply a function to each element, row, or column of the DataFrame.
# of course there are more
# NumPy is a library used for working with arrays, linear algebra, fourier transform, and matrices. 
# It's usually imported under np alias = import numpy as np, NUMPY ARRAYS MUST CONTAIN ELEMENTS OF THE SAME TYPE
# APIs, or Application Programming Interfaces allow developers to create new applications by leveraging existing functionality from other systems
# Important because allow to access data and functionality from other systems, which can save time and resources because we don't have to write new code from skratch
# MORE INFO IN READINGS FOR COURSE 2
# 
