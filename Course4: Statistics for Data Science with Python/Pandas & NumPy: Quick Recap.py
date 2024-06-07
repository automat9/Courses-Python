#---------------------------------------------------------------------------------------------------------------------------------------------------
# DATA ACQUISITION
#---------------------------------------------------------------------------------------------------------------------------------------------------

import piplite
await piplite.install(['numpy'],['pandas'])

# import library
import pandas as pd
import numpy as np

# use pandas.read_csv() to read a csv file, in bracket we put the file path along with a quotation mark, either URL
# or local file address  if data doesn't include headers, we can add an argument headers = None, inside the read_csv() method,
# so that pandas won't automatically set the first row asa header
from js import fetch
import io

URL = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
resp = await fetch(URL)
other_path = io.BytesIO((await resp.arrayBuffer()).to_py())

# Read the online file by the URL provides above, and assign it to variable "df"
df = pd.read_csv(other_path, header=None)
df

# dataframe.head(n) where n is an integer shows top n rows, dataframe.tail(n) will do the same but with bottom n rows
print("Here are the first 3 rows of the dataframe :)")
df.head(3)

# If you look at the dataset above, you'll find that the header was automatically set as a number starting from 0, let's change that
# To add headers, first create a headers list:
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

# Now to change the headers:
df.columns = headers
df.head(10) # to check the results
df.columns # again, this will show the new column list

# Dataset has missing values "?", replace them with NaN so the dropna() can remove the missing values
df1=df.replace('?',np.NaN)
# To drop missing values along the column "price":
df=df1.dropna(subset=["price"], axis=0)
df.head(20) # to check the results

# to save the dataset
df.to_csv("automobile.csv", index=False) # to_csv, if we were to pd.read_excel() we would have df_to_excel(), saving file as "automobile"
#---------------------------------------------------------------------------------------------------------------------------------------------------
# BASIC INSIGHT OF DATASET
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Data Types in each column
df.dtypes

# Statistical summary of each column
df.describe() # this only shows numeric-typed columns (int, float), if we also want object columns to be included, do:
df.describe(include = "all") # some values are shown as "NaN" because those numbers are not available regarding a particular column type

# To find specific columns, do dataframe[["column 1", "column 2", "column 3" etc]], e.g.
df[["symboling","make"]]
# To find statistics about specifc column/s
df[["length", "compression-ratio"]].describe()

# Info is another method to find concise summary of your dataset, info includes index, dtype, columns, non-null values and memory usage
df.info() # remember, default method is dataframe.info(), but we used a variable df instead for convenience :)
