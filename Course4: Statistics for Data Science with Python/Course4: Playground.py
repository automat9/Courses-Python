# =================== Intro to Statistics ==========================================================================================================================================================================================================================================================
# Types of statistical data
# Cross-sectional = measurement taken at one time period, e.g.students evaluating a course
# Time series - data collected over time, e.g. uneployment rate

# Number of variables
# Univariate - data consisting of a single variable to measure some entity
# Multivariate - data consisting of two or more variables to measure some entity

# Variable types
# Categorical (nominal) - sorted into mutually exclusive categories, e.g. own or rent a flat, mode of travel, gender, type of employment, NO QUANTITIATIVE RELATIONSHIPS AMONG CATEGORIES AND AVERAGES ARE USUSALLY MEANINGLESS
# Ordinal - ordered according to some relationship to one another, e.g. number of cars owned by a household, categories can be compared with one another, usually meaningless because no fixed units of measurement, i.e. differences are meaningless
# Ratio - data with no natural zero, e.g. sales dollars, length, weight, time from start of a process, business data, strongest form of measurement, both ratios and differences are meaningful
# Interval - ordered and characterised by a specific measure of distance between observations, but with no natural zero, e.g. temperature, time, survey scales, ratios are meaningless (50 degrees is not twice as hot as 25 degrees), differences are meaningful, so averages can be compared

# 1) use df.info() to find columns and their data types
# 2) use df.describe() to find: Mean, sd. itq.range and min/max values

# ==================================== #
# Measures of central tendency
# x̄ - Sample mean
# Σ - Operation of addition ("the sum of")
# N - size of population
# n - size of sample
# ==================================== #
# Measures of Dispersion
# Dispersion - degree of variation in the data (is the majority of data in one place, or is it spread out)
# Low SD =  more consistency, majority of values close to each other, high SD means larger spread from the mean
# e.g. 2 datasets, 1) mean 10, sd 0 = 10, 10, 10, 2) mean 10, sd 10 = 0, 10, 20
# REMEMBER: average = partial picture, avg. statistics are incomplete without SD/var, risk metrics are ALL ABOUT VARIANCE!
# Range - max - min = range
# ==================== Let the fun begin :) =========================================================================================================================================================================================================================================================

# Import libraries and read the csv file from the URL (copied code from labs)

import piplite
await piplite.insall(["numpy"],["pandas"])

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
resp = await fetch(URL)
ratings_url = io.BytesIO((await resp.arrayBuffer()).to_py())

ratings_df=pd.read_csv(ratings_url) # now very important, ratings_df will now be used as a variable for all the other commands
# ==================== Basic Info =====================================================
ratings_df.head() # shows first five rows of the data
ratings_df.head(25) # first 25
ratings_df.trail(25) # last 25

ratings_df.info() # shows info about each variable - (non-null count, data type(obj,int,float, etc))

ratings_df.shape # prints as (number of rows, no. of columns)

# The dataset  is cross-sectional because - no time variable, observes multiple persons and compares them at one point in time

# ==================== Measures of central tendancy (really cool stuff :)) =====================================================

ratings_df.describe() # describes the whole dataset
ratings_df['students'].describe() # you're never gonna believe which column this code describes

# ohhh, you're only interested in individual measures, alright then:
ratings_df['students'].mean()
ratings_df['students'].median()
ratings_df['students'].mode()
ratings_df['students'].min()
ratings_df['students'].max()
# happy?

# Now let's create a histogram :D
pyplot.hist(ratings_df['beauty'])
# Now let's create a bar chart :D
pyplot.bar(ratings_df.gender.unique(), ratings_df.gender.value_counts(),color=["pink","blue"])
pyplot.xlabel('Gender')
pyplot.ylabel('Count')
pyplot.title('Gender distribution bar plot')

# create a table to compare genders and their beauty results
ratings_df.groupby('gender').agg({'beauty':['mean', 'std', 'var']}).reset_index() 

# calculate the percentage of males and females that are tenured professors.
# first groupby to get the total sum
tenure_count = ratings_df[ratings_df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()
# find %
tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count

# To find median evaluation score for tenured professors (the tricky part is that this is not a numerical value)
ratings_df[ratings_df['tenure'] == 'yes']['eval'].median()
# you can index just tenured professors and find their median evaluation scores

# To compare avg age with tenure, to produce the means and sd for both tenured and unt. professors:
ratings_df.groupby('tenure').agg({'age':['mean', 'std']}).reset_index()


# ==================== Visualization Fundamentals =====================================================

# WHat can be visualised:
# Distribution - e.g. scatter (if 2 var.), bell curve, histogram
# Comparison - bar, line, circular area chart
# Composition - e.g. pie
# Relationship - e.g. bubble (3 variables, x, y axes and size being third var) or scatter (2 var)

# seaborn and matplotlib will be used

# ==================== Lab ============================================================================

# Import libs

import piplite
await piplite.install(['numpy'])
await piplite.install(['pandas'])
await piplite.install(['seaborn'])

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

from js import fetch
import io
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
resp = await fetch(URL)
ratings_url = io.BytesIO((await resp.arrayBuffer()).to_py())

ratings_df = pd.read_csv(ratings_url) # read the file

ratings_df.prof.unique() # identifies all duplicate cases of the prof variables, (array with 
ratings_df.prof.nunique() # prints out the number of unique values in the prof variable

# let's find avg and std for age
ratings_df["age"].mean()
ratings_df["age].std()

# Filter the data set to include one observation for each instructor with a total number of observations restricted to 94
no_duplicates_ratings_df = ratings_df.drop_duplicates(subset =["prof"]
no_duplicates_ratings_df.head()

# new avg and std for age
no_duplicates_ratings_df['age'].mean()
no_duplicates_ratings_df['age'].std()








# ==================== Probability Distribution =======================================================

# Probability is a measure between o and 1 of the likelihood that an event might occur (duh)
# Random variable is a variable with an unknown value OR a function that assigns values to each of an experiment's outcomes (I knew that)

# Hypotheses & Distribution: 
# α significance level = probability of rejecting the null hyp. when the null hyp. is true
# p-value = probability of getting a result that is as extreme or more extreme when the null hyp. is true
# T-distribution = describes mean of samples drawn from a population (whereas normal dist describes mean for population)
# T-test = testing for statistical significance (assumptions: continous or ordinal scale, random sample, bell-shape, homogeneity of variance - to avoid bias towards large sample sizes)

# ==================== Lab ============================================================================

# Import libraries and read the csv lab file
import piplite
await piplite.install(['numpy'])
await piplite.install(['pandas'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from math import sqrt

from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
resp = await fetch(URL)
ratings_url = io.BytesIO((await resp.arrayBuffer()).to_py())

ratings_df = pd.read_csv(ratings_url)

# ==== Creating normal distribution =========================================

# Pmport norm from scipy.stats and plot using matplotlib
from scipy.stats import norm

# Plot between -4 and 4 with 0.1 steps.
x_axis = np.arange(-4, 4, 0.1)
# Mean = 0, SD = 1.
plt.plot(x_axis, norm.pdf(x_axis, 0, 1))
plt.show()

