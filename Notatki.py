# integer e.g. 1,3,4,5  = int
# real number e.g. 1.4, 54.22, 9493,34555 = float
# string e.g. "Hello World" = str
# boolean = True(1)/False(0) = bool (upper case mandatory)
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
