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

# ==================== Plotting data ==================================================================
# ======== BAR CHART ========
# Use a bar chart to demonstrate if instructors teaching lower-division courses receive higher avg teaching evaluations
ratings_df.head()

# Find avg teaching evaluation in both groups of upper and lower-division
division_eval = ratings_df.groupby('division')[['eval']].mean().reset_index() # this finds the avg eval. in both groups of upper and lower div

# Plotting the barplot using the seaborn library
sns.set(style="whitegrid")
ax = sns.barplot(x="division", y="eval", data=division_eval)
plt.show()

# ======== SCATTER DIAGRAM ==
# to plot the relationship between age and teaching evaluations
ax = sns.scatterplot(x='age', y='eval', data=ratings_df)
plt.show()

# to do the above + show difference between the two genders
ax = sns.scatterplot(x='age', y='eval', hue='gender',
data=ratings_df)
plt.show()

# ======== BOX PLOT =========
# for beauty scores differentiated by credits
ax = sns.boxplot(x='credits', y='beauty', data=ratings_df)
plt.show()

# age of instructor by gender
ax = sns.boxplot(x="gender", y="age", data=ratings_df)
plt.show()

# compare age along with tenure and gender
ax = sns.boxplot(x="tenure", y="age", hue="gender",
data=ratings_df)
plt.show()

# Horizontal box plot of age of instructors by visible minority (whether horizontal or vertical depends on position of argument ( which one is x and which one is y))
ax = sns.boxplot(y="minority", x="age", data=ratings_df)
plt.show()

# Boxplot of the age variable, y axis can be changed to x depending on which one you prefer
sns.boxplot(y="age", data=ratings_df)
plt.show()

# ======== CATPLOT ========== (meow)
# to count how many courses are taught by gender
sns.catplot(x='gender', kind='count', data=ratings_df)
plt.show()

# creating a group histogram by adding hue = tenure
sns.catplot(x='gender', hue = 'tenure', kind='count', data=ratings_df)
plt.show()

# Adding division as another factor to the same histogram (now we have 2 rows)
sns.catplot(x='gender', hue = 'tenure', row = 'division',
            kind='count', data=ratings_df,
            height = 3, aspect = 2)
plt.show()

# Grouped bar plot of tenure by minority with gender as factor
sns.catplot(x='tenure', hue = 'minority', row = 'gender', kind='count', data=ratings_df, height = 3, aspect = 2)
plt.show()

# ======== RELPLOT ==========
# Complex scatter plot - creates a scatterplot of age and evaluation scores, differentiated by gender and tenure)
sns.relplot(x="age", y="eval", hue="gender",
            row="tenure",
            data=ratings_df, height = 3, aspect = 2)
plt.show()

# ======== DISTRIBUTION =====
ax = sns.displot(ratings_df['eval'], kde = False) # kde creates a curve :D
plt.show() # old versions of seaborn use distplot instead of displot

# Creating 2 distribution plots of teaching evaluation score with gender as a factor
sns.displot(ratings_df[ratings_df['gender'] == 'female']['eval'], color='green', kde=False) 
sns.displot(ratings_df[ratings_df['gender'] == 'male']['eval'], color="orange", kde=False) 
plt.show()

# Creating 2 distribution plots of beauty scores with native eng speaker as a factor
sns.displot(ratings_df[ratings_df["native"] == "yes"]["beauty"], color="orange")
sns.displot(ratings_df[ratings_df["native"] == "no"]["beauty"], color="green")
plt.show()

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

# ===== Probability of receiving an evaluation score of greater than 4.5 =====

# 1) find the mean and std of teachers' evaluation scores
eval_mean = round(ratings_df['eval'].mean(), 3)
eval_sd = round(ratings_df['eval'].std(), 3)
print(eval_mean, eval_sd)

# 2) Use scipy.stats, because Python only looks to the left (X<x) we remove the probability from 1 to get the other side of tail
prob0 = scipy.stats.norm.cdf((4.5 - eval_mean)/eval_sd)
print(1 - prob0)

# ===== Again =========================================================================

# calculate the probability less than 3.3
prob_less_than = scipy.stats.norm.cdf((3.3 - eval_mean)/eval_sd)

# then remove the probability from 1 to get the area to the right of 3.3
print(1 - prob_less_than)

# ===== Probability of receiving an evaluation greater than 3.5 and less than 4.2 =====

# 1) first find prob of getting eval score less than 3.5 using norm.cdf
x1 = 3.5
prob1 = scipy.stats.norm.cdf((x1 - eval_mean)/eval_sd)
print(prob1)

# 2) then for less than 4.2
x2 = 4.2
prob2 = scipy.stats.norm.cdf((x2 - eval_mean)/eval_sd)
print(prob2)

# 3) prob of receiving eval score between 3.5 and 4.2 is:
round((prob2 - prob1)*100, 1)

# ==== Again =============================================================================
# Probability of receiving a score between 2 and 3
x1 = 2
less_than_2 = scipy.stats.norm.cdf((x1 - eval_mean)/eval_sd)
print(prob1)

x2 = 3
less_than_3 = scipy.stats.norm.cdf((x2 - eval_mean)/eval_sd)
print(prob2)

round((less_than_3 - less_than_2)*100,1)

# ==== One-tailed test from a normal distribution ===========================
# Hypothesis - sleeping for 8 hours makes one smarter, 12 people have their iq tested: 
# H0: u = 100, Ha u>100

iqs = [116,111,101,120,99,94,106,115,107,101,110,92]
sample_size = len(iqs)
degree_freedom = sample_size - 1
iq_mean = sum(iqs) / sample_size
mean_diff = [(iq - iq_mean) ** 2 for iq in iqs]
iq_std = sqrt(sum(mean_diff) / degree_freedom)
variance = iq_std ** 2

round(1 - scipy.stats.norm.cdf((iq_mean - 100)/(iq_std/sqrt(12))), 3)

result is 0.009, which is smaller than the standard 5% sig level (0.05), meaning that the null hypothesis can be rejected 

# ==== Two-tailed test from a normal distribution ===========================

# pro players vs regional players
# pros have historic mean of 12 per game and std of 5.5
# group of 36 regional players have avg of 10.7 points per game
# are pro scores different from the regional players?

# Null = H_0 x = u_1
# Alt = H_1 x =/ u_1

# because it is a two-tailed test we multiply by 2
2*round(scipy.stats.norm.cdf((10.7 - 12)/(5.5/sqrt(36))), 3)

# concl + p-value greater than 0.05, we fail to reject null

# ==================== Hypothesis Testing =============================================================

# Import libraries (the commented ones are preinstalled on Skills Network, but you have to uncomment them)

#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#! mamba install scipy=1.7.1-y
#!  mamba install seaborn=0.9.0-y
#!  mamba install matplotlib=3.4.3-y
#!  mamba install statsmodels=0.12.0-y

import piplite
await piplite.install(['numpy'],['pandas'])
await piplite.install(['seaborn'])

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats

from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
resp = await fetch(URL)
ratings_url = io.BytesIO((await resp.arrayBuffer()).to_py())

ratings_df = pd.read_csv(ratings_url)

# ===== T-Test: Does gender affect teaching evaluations? =====

# H_0 : μ_1 = μ_2 (no difference in evaluation scores between males and females)
# H_1 : μ_1 ≠ μ_2 (difference in evaluation scores - two-tailed)

# Plotting dependent variable with a histogram:
ax = sns.distplot(ratings_df['eval'],
                  bins=20,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

# Use Levene's test to check test significance (since p-value is greater than 0.05, we can assume equality of variance)
scipy.stats.levene(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], center='mean')

# Actual T-test - p-value is less than 0.05 and thus we reject the null hypothesis
scipy.stats.ttest_ind(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], equal_var = True)
                   
# ===== T-Test: Does tenure affect teaching evaluations? =====
scipy.stats.ttest_ind(ratings_df[ratings_df['tenure'] == 'yes']['eval'],
                   ratings_df[ratings_df['tenure'] == 'no']['eval'], equal_var = True)

# ===== ANOVA: Does beauty score for instructors differ by age =====

# H_0 : μ_1 = μ_2 = μ_3 (three population means are equal)
# H_1 : At least 1 of the means differ

# Test for equality of variance
scipy.stats.levene(ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty'],
                   ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty'], 
                   ratings_df[ratings_df['age_group'] == '57 years and older']['beauty'], 
                   center='mean')
# since the p-value is less than 0.05, the variance are not equal, for the purposes of this exercise, we will move along

# Separate the three samples (one for each job category) into a variable each
forty_lower = ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty']
forty_fiftyseven = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty']
fiftyseven_older = ratings_df[ratings_df['age_group'] == '57 years and older']['beauty']

# Now run a one-way ANOVA
f_statistic, p_value = scipy.stats.f_oneway(forty_lower, forty_fiftyseven, fiftyseven_older)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
# p-value is less than 0.05, thus we reject the null hypothesis in favour of the alternative hypothesis (at least one of the means differ)

# ===== ANOVA: Does teaching evaluation score for instructors differ by age =====
# Again, test for equality of variance
scipy.stats.levene(ratings_df[ratings_df['age_group'] == '40 years and younger']['eval'],
                   ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['eval'], 
                   ratings_df[ratings_df['age_group'] == '57 years and older']['eval'], 
                   center='mean')
# p-value = 0.02, so lower than 0.05

# Assigning variables
forty_lower_eval = ratings_df[ratings_df['age_group'] == '40 years and younger']['eval']
forty_fiftyseven_eval = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['eval']
fiftyseven_older_eval = ratings_df[ratings_df['age_group'] == '57 years and older']['eval']

# One way ANOVA
f_statistic, p_value = scipy.stats.f_oneway(forty_lower_eval, forty_fiftyseven_eval, fiftyseven_older_eval)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
# p-value = 0.2954, so we fail to reject the null hypothesis

# ===== Chi-square: Is there an association between tenure and gender =====
 # H_0: The proportion of teachers who are tenured is independent of gender
 # H_1: The proportion of teachers who are tenured is associated with gender

# Create a cross-tab table
cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['gender'])
cont_table

# Use the scipy.stats library and set correction equals False as that will be the same answer when done by hand, 
# it returns: 𝜒2 value, p-value, degree of freedom, and expected value
# Actual test below
scipy.stats.chi2_contingency(cont_table, correction = False)

# p-value greater than 0.05, we fail to reject null, no sufficient evidence that teachers are tenured as a result of gender

# ===== Chi-square: Is there an association between age and tenure =====
# Test
cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['age_group'])
scipy.stats.chi2_contingency(cont_table)

# ===== Chi-square: Is there an association between visible minorities and tenure =====
# Test
cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['vismin'])
scipy.stats.chi2_contingency(cont_table)

# ===== Correlation: Is teaching evaluation score correlated with beauty score =====
 # H_0: Teaching evaluation score is not correlated with beauty score
 # H_1: Teaching evaluation score is correlated with beauty score

# Both are continous variables, we can use a pearson correlation test and draw a scatter plot
ax = sns.scatterplot(x="beauty", y="eval", data=ratings_df)

# Actual test:
scipy.stats.pearsonr(ratings_df['beauty'], ratings_df['eval'])
# p is less than 0.05, we reject null and conclude that there is a relationship between beauty and teaching evaluation score

# ======================= BONUS LEVENE TEST ===========================
# equality of variance for beauty scores between tenured and non-tenured instructors
scipy.stats.levene(ratings_df[ratings_df['tenure'] == 'yes']['beauty'],
                   ratings_df[ratings_df['tenure'] == 'no']['beauty'], 
                   center='mean')


# ==================== Regression Analysis ============================================================
# Import libraries (again)

# commented are already installed on skills network
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#! mamba install scipy=1.7.1-y
#!  mamba install seaborn=0.9.0-y
#!  mamba install matplotlib=3.4.3-y
#!  mamba install statsmodels=0.12.0-y

import piplite
await piplite.install(['numpy'],['pandas'])

import numpy as np
import pandas as pd
import statsmodels.api as sm

from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
resp = await fetch(URL)
ratings_url = io.BytesIO((await resp.arrayBuffer()).to_py())

ratings_df = pd.read_csv(ratings_url)


# Regression with t-test:
# Question: Using the teachers rating data set, does gender affect teaching evaluation rates?
# Hypothesis: 
# H_0: β1 = 0 (Gender has no effect on teaching evaluation scores)
# H_1: β1 ≠ 0 (Gender has an effect on teaching evaluation scores)
-------
## X is the input variables (or independent variables)
X = ratings_df['female']
## y is the target/dependent variable
y = ratings_df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
-------
# Conclusion: Like the t-test, the p-value is less than the alpha (α) level = 0.05,
so we reject the null hypothesis as there is evidence that there is a difference in mean evaluation scores based on gender.
The coefficient -0.1680 means that females get 0.168 scores less than men.


# Regression with ANOVA:
# Questions: does beauty score for instructors differ by age? 
# Hypothesis: 
# H_0 : μ_1 = μ_2 = μ_3 (three population means are equal)
# H_1 : At least 1 of the means differ
-------
# Group data like with did with ANOVA
ratings_df.loc[(ratings_df['age'] <= 40), 'age_group'] = '40 years and younger'
ratings_df.loc[(ratings_df['age'] > 40)&(ratings_df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
ratings_df.loc[(ratings_df['age'] >= 57), 'age_group'] = '57 years and older'

# Perform regression:
from statsmodels.formula.api import ols
lm = ols('beauty ~ age_group', data = ratings_df).fit()
table= sm.stats.anova_lm(lm)
print(table)
--------
# Conclusion: same value for anova like before - PR(>F), so we reject null

# OPTION 2:
# Create dummy variables (numeric variables that represent categorical data, such as gender, race etc, they can only take 2 quantitative units)
X = pd.get_dummies(ratings_df[['age_group']])
y = ratings_df['beauty']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary() # same results and conclusion as OPTION 1


# Regression with correlation: 
# Question: Is teaching evaluation score correlated with beauty score?
# No hypothesis, straight onto the statistics
------
## X is the input variables (or independent variables)
X = ratings_df['beauty']
## y is the target/dependent variable
y = ratings_df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
-------
# Conclusion: p<0.05, so evidence of correlation between beauty and eval scores


# Practice Questions:

# 1) Does tenure affect beauty scores?
X = pd.get_dummies(ratings_df[['tenured_prof']]) # using dummy variable because OLS lib doesn't recognise texts
y = ratings_df['beauty']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

model.summary()

# 2) Does being an English speaker affect 
X = ratings_df['English_speaker']
y = ratings_df['allstudents']
# adding an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

model.summary()

# 3) what is the correlation between no. of students who participated in the eval survey and eval scores?

X = ratings_df['students']
y = ratings_df['eval']
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

model.summary()
# HERE, FOCUS ON R-SQUARE, NOT P>t or T, IF YOU TAKE SQUARE ROOT OF R YOU GET HOW STRONG THE CORRELATION IS (v. weak)

