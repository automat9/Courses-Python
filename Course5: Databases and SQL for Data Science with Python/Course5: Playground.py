#============================================ Module 1 =======================================================================
# SQL is a language used for relational databases to get data out of a database
# What data? Facts (words, numbers), Pictures, Assets
# What is a database? Repository of data, provides functionality for adding, modyfing and querying that data
# Basic SQL commands: Create a table, insert, select and update

# Select: 
SELECT COLUMN1, COLUMN2, ... FROM TABLE_1 ; # General syntax
SELECT * FROM TABLE_1 ; # To retreive all columns
SELECT <COLUMNS> FROM TABLE_1 WHERE <predicate> ; # To filter data based on a predicate
# e.g. to select first 5 rows: SELECT * FROM TABLE_1 WHERE ID <= 5 ;
# another e.g.: select * from FilmLocations where Locations = 'City Hall'

# Count:
# Retreives number of rows that matches the query criteria (NOT ROW CONTENT, JUST HOW MANY ROWS MATCH THE CRITERIA)
select COUNT(COUNTRY) from MEDALS where COUNTRY = 'CANADA' 

# Distinct:
# Removes duplicate values from a result set
select DISTINCT COUNTRY from MEDALS where MEDALTYPE = 'GOLD' # In case some countries receive multiple gold medals

# Limit:
# Restricts the number of rows retreived from the database
select * from tablename LIMIT 10
select * from MEDALS where YEAR = 2018 LIMIT 5 # shows 5 rows in the MEDALS table for a particular year

# Insert:
# Add new rows to a table
insert into tablename (Name, Surname, Age) values ('Mateusz', 'Pawlaczyk', 20) # IMPORTANT no. of columns must = to no. of values
# we can also add multiple rows to our Name, Surname, Age columns, just do another bracket () under the one above

# Update:
# Welp it updates a row
UPDATE tablename SET Columnname = Value WHERE condition # if you don't specify where, all the rows will be updated
# UPDATE Author SET Lastname='KATTA', FIRSTNAME='Lakshmi' WHERE Author_ID='A2'

# Delete
# deletes rows
DELETE FROM Author WHERE Author_ID IN ('A2','A3') # if you don't specify where, all rows will be removed (careful buddy)

#============================================ Module 2 =======================================================================
# Data Definition Language (DDL) Statements
# Used to define, change, or drop data - tables
# E.g. CREATE, ALTER, TRUNCATE, DROP


# Data Manipulation Language (DML) Statements
# Used to read and modify data - rows
# E.g. INSERT, SELECT, UPDATE, DELETE - row (like in module 1)

11min
