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
20min
