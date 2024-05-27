#--------------------------IF STATEMENTS--------------------------#
name = "Mateusz Pawlaczyk" # Assigning name to variable
if name: # the logic here is that "if name is True" (has a value/isn't empty i.e. name = "")
    print("My name is:", name)
# This can be rewritten as:
name = "Reddosław Czerwiński"
if name == name: # this is a bit unintuitive but it checks if the value of name is exactly equal to name, which in this case means the same as name == "Reddosław Czerwiński"
    print(name)


