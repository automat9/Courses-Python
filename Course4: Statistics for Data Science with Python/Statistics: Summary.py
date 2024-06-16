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
# 1) use when population std is unknown
# 2) also when comparing the means of 2 independent samples with equal or unequal variances

# ANOVA (Analysis of Variance)
# 1) used if dealing with more than 2 groups - comparing means of more than 2 groups
# 2) for this, we use F-distribution to compare the mean values for more than 2 groups
# 3) null = samples in all groups are drawn from the same populations with the same mean values
# 4) reject null = if p-value or sig for f-test is less than 0.05

# Chi-square test for Association
# e.g. testing for relationships between categorical variables
# 1) null: no association between x and y
