# Goal of hypothesis testing: to answer the question "given a sample and an apparent effect, what is the probability of seeing such an effect by chance"
# Step 1) Quantify the size of the apparent effect by choosing a test statistic (e.g. t-test, ANOVA, Chi-square, etc.)
# Step 2) Define a null hypothesis (a model of the system based on the assumption that the apparent effect is not real)
# Step 3) Compute the p-value (probability of null being true)
# Step 4) Interpret the result of the p-value (if low, the effect is said to be statistically significant, i.e. reject null)

# Z-score = (X - μ)/σ - i.e your score - population mean / standard deviation

# Z-test
# 1) use when population std is known

# T-test - comparison of average values between 2 groups
# e.g. testing if teaching evaluations of male instructors are the same for female instructors
# Assumptions:
# 1) One independent, categorical variable with two levels or group
# 2) One dependent continous variable
# 3) Independence of the observations. Each subject should belong to only one group. There is no relationship between the observations in each group.
# 4) The dependent variable must follow a normal distribution
# 5) Assumption of homogeneity of variance
# Also use when population std is unknown
# AND when comparing the means of 2 independent samples with equal or unequal variances

# ANOVA (Analysis of Variance)
# Used if dealing with more than 2 groups - comparing means of more than 2 groups
# Can't work with continous variable, which is why we need to create categories
# e.g. Does beauty score for instructors differ by age (instead of 50,51,52 years, we can create 3 age categories, 51-60, 61-70, 71-80)
# for this, we use F-distribution to compare the mean values for more than 2 groups
# 1) null = samples in all groups are drawn from the same populations with the same mean values
# 2) reject null = if p-value or sig for f-test is less than 0.05


# Chi-square test for Association (association is the key word, if you hear it, it's chi square)
# e.g. testing for relationships between categorical variables - correlation
# 1) null: no association between x and y

# Pearson correlation test (also correlation)
# Use for continous variables, like age, beauty score, evaluation score etc

# Levene's test for equality of variance
# e.g. important in T-test or ANOVA as it tests the assumption of homogeneity of variance
# If less than 0.05 then the two variances are significantly different
# If more than 0.05 then the two variances are statistically equal


# Regression: the ultimate tool for hypothesis testing, can arguably replace t-test, ANOVS or pearson correlation test
# 1) we need a question: e.g. does x decrease with y, do x people get paid more than y people, association between x and y?
# 2) identify dependent (one that we're interested in) and explanatory (those that influence the dependent) variables
# 3) x = explanatory, y = dependent
# 4) correlation coefficient is r-squared value, but square rooted

# Regression in place of a t-test:
# 1) is there a statistically significant difference in teaching evaluation scores for men and women?
# 2) create a list for independent variable (female) and dependent variable (score)
# 3) run model and interpret results, looking at t value and P>¦t¦, if less than 0.05 then reject null
# 4) say you want to find out if there's diff. in no. of students enrolled with professors who are visible minority
# 4a) where vismin = 1 and not visible minority = 0, the coefficient for vismin after test is -21, that means:
# 4b) they get on avg. 21 students less than profs who aren't visible minority

# Regression in place of ANOVA:
# 1) does beauty score for instructors differ by age?
# 2) ANOVA requires to cetegorise age into age ranges, then use OLS function to test:
ratings_df.loc[(ratings_df['age'] <= 40), 'age_group'] = '40 years and younger'
ratings_df.loc[(ratings_df['age'] > 40)&(ratings_df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
ratings_df.loc[(ratings_df['age'] >= 57), 'age_group'] = '57 years and older'

from statsmodels.formula.api import ols
lm = ols('beauty ~ age_group', data = ratings_df).fit()
table= sm.stats.anova_lm(lm)
print(table)
