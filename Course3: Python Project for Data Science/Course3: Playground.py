#-------------------------------------------------------------------------------------------------------------
# Extracting Stok Data using yFinance, a Python Library
!pip install yfinance==0.2.4
!pip install pandas==1.3.3
import yfinance as yf
import pandas as pd
import json
# using the yfinance Library to Extract Stock Data
# the Ticker module allows us to create an object to access functions to extract data, we need to provide the ticker symbol for the stock
apple = yf.Ticker("AAPL")

# Useful website: https://aroussi.com/post/python-yahoo-finance
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json # this only works on skills labs
# using "info" we can extract information about the stock as a Python dictionary
with open("apple.json") as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
print("Type: ", type(apple_info)) # returns Type: <class 'dict'>
apple_info['country'] # using the key country we can find useful info

# Extracting Share Price 
apple_share_price_data = apple.history(period="max")
# history() allows us to get the share price of the stock over a certain period of time
# using the period parameter we can set how far back from the present to get data, options are:
# 1 day (1d) 5d, 1 month (1mo), 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, and max

apple_share.price_data.head()
# data is returned in a Pandas Dataframe. With the Date as the index, the columns are: open, high, low, close, volume and stock splits for each day
apple_share.price_data.head(2) # doesn't return a table but rather a specific row (useful :))

apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.head()
# this will reset the index, inplace set to true means the change will take place to the DataFrame itself
# in other words the date column will no longer be treated as index, instead an additional column will appear on the left with the actual index list

apple_share_price_data.plot(x="Date", y="Open")
#  Plotting the Open prices againast the Date (very fun :))

apple.dividends # company profits returned per share an investor owns, period defined in the "history" function
apple.dividends.plot() # guess what, this will plot the dividends over time :O

#-------------------------------------------------------------------------------------------------------------
# Extracting Stock Data using Web Scraping
# We have to use this as well as not all stock data is available via the API in the assignment, historical data will be extracted using beautiful soup
!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y 
!pip install lxml==4.6.4
!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

# To ignore warnings:
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Scenario - using yahoo finance website and looking to extract Netflix Data
# we want to extract: date, open, high, low, close and volume

# Steps for extracting the data
# 1. Send an HTTP request to the web page using the requests library.
# 2. Parse the HTML content of the web page using BeautifulSoup.
# 3. Identify the HTML tags that contain the data you want to extract.
# 4. Use BeautifulSoup methods to extract the data from the HTML tags.
# 5. Print the extracted data

# Step 1
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
print(data)
# requests.get() takes a URL as its first argument, this specifies the location of the resoruce, .text is used for extracting the HTML as a string in order to read it
# the result is a veeeeery long and messy string of text, its difficult to understand and read, so let's parse it :)

# Step 2
# let's recap: parsing is the process of analysing a string or a data structure to understand its meaning. 
# it involves breaking down a piece of text or data into its individual componenets or elements, and then analysing them to extract
# the desired information, or to understand their relationships and meaning
# after running the cell, you'll find that the result is still quite difficult to read, but it'll be easier to manipulate in Python
soup = BeautifulSoup(data, 'html5lib')
# 2 arguments to constractor:
# a) the html or xml content that you want to parse
# b) name of the parser that you want to use to parse the content, this is optional, if left blank BeatifulSoup will use the default included in library

# Step 3
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"]) # creating empty DataFrame
# tags that are used while creating HTML tables:
# <table> - root tag used to define the star and end of the table, everything is enclosed within these
# <tr> - used to define table row, each row is defined within this tag
# <td> - used to define a table cell
# <th> - used to define a header cell in the table, by default bold and centred, used to describe contents of column or row
# <tbody> - main content of table, contains one or more rows of elements

# Step 4
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'): # find returns particular tag content, find all returns a list of all matching tags in the HTML
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

# Step 5
netflix_data.head() # :)
#-------------------------------------------------------------------------------------------------------------
# Extracting data using Pandas library
pd.read_html(url) # read_html function is used to extract tables from HTML web pages, takes URL as input and returns a list of all the tables found on the page

read_html_pandas_data = pd.read_html(str(soup)) # you can convert the BeautifulSoup object to a string

netflix_dataframe = read_html_pandas_data[0] # only one table on the page so just find [0]

netflix_dataframe.head()

# Excercise
# 1. Using requests, dowlonad the webpage: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html.
#    save the text of the response as a variabe named html_data
# 2. Parse the html data using beautiful_soup
# 3. Q1: What is the content of the title attribute?
# 4. Using BS, extract the table with historical share prices and store it into a dataframe named amazon_data
# 5. Print out the first five rows of the amazon_data dataframe
# 6. Q2: What are the names of the columns in the dataframe?
# 7. Q3: What is the "Open" of the last row of the amazon_data dataframe?
FINISH THIS (important)
