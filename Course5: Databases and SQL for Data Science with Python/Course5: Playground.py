#============================================ Module 1 =======================================================================
# SQL is a language used for relational databases to get data out of a database
# What data? Facts (words, numbers), Pictures, Assets
# What is a database? Repository of data, provides functionality for adding, modyfing and querying that data
# Basic SQL commands: CREATE, SELECT, INSERT, UPDATE, DELETE

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

# Create:
# Syntax: 
CREATE TABLE table_name
    (
      column_name_1 datatype optional_parameters,
      column_name_2 datatype,
      column_name_n datatype
    )
# datatypes include: CHAR(2) - string of fixed length 2 AND VARCAHAR(14) - variable length, up to 14 chatacters long
# optional parametrs include: PRIMARY KEY (prevents dulicates in the table), NOT NULL

# Alter:
# Add/remove columns, keys, constraints, or modify datatype
# Syntax:
ALTER TABLE <your_table_name> # and then, same line either:
ADD COLUMN <column_name_n> datatype
MODIFY <column_name_n> <data_type>
 # To change the data type of an existing column to varchar data type write:
ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE VARCHAR(20);
#  To add a column ‘ID’ that contains 7 character alpha-numeric values to our database
ALTER TABLE Employees ADD ID char(7)


# Drop (delete)
DROP TABLE <table name>;
DROP COLUMN <column_name_n>

# Truncate (delete data in table without deleting table itself)
TRUNCATE TABLE <table_name>
  IMMEDIATE # specifies to process statement immediately, cannot be undone)

# SCENARIO:
# create a table with CREATE
# ALTER - create a new column
# UPDATE - add values e.g. update petsale set quantity = 24 where ID = 1
# after each modification, use select * from petsale to SEE THE TABLE (otherwise won't show up)

