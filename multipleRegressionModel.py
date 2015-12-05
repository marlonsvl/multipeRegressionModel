# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:01:26 2015

@author: marlon
"""

import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

data = pandas.read_csv('/Users/utpl/Documents/RegressionModelingInPractice/gapminder.csv')

# convert to numeric format
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy'], errors='coerce')
data['breastcancerper100th'] = pandas.to_numeric(data['breastcancerper100th'], errors='coerce')
data['hivrate'] = pandas.to_numeric(data['hivrate'], errors='coerce')


# listwise deletion of missing values
sub1 = data[['lifeexpectancy', 'breastcancerper100th', 'hivrate']].dropna()

####################################################################################
# POLYNOMIAL REGRESSION
####################################################################################

# first order (linear) scatterplot
scat1 = seaborn.regplot(x="breastcancerper100th", y="lifeexpectancy", scatter=True, data=sub1)
plt.xlabel('Life Expectancy')
plt.ylabel('Breast Cancer per 100th')

# fit second order polynomial
# run the 2 scatterplots together to get both linear and second order fit lines
scat1 = seaborn.regplot(x="breastcancerper100th", y="lifeexpectancy", scatter=True, order=2, data=sub1)
plt.xlabel('Life Expectancy')
plt.ylabel('Breast Cancer per 100th')

# center quantitative IVs for regression analysis
sub1['breastcancerper100th_c'] = (sub1['breastcancerper100th'] - sub1['breastcancerper100th'].mean())
sub1['lifeexpectancy_c'] = (sub1['lifeexpectancy'] - sub1['lifeexpectancy'].mean())
sub1[["breastcancerper100th_c", "lifeexpectancy_c"]].describe()


# linear regression analysis
reg1 = smf.ols('lifeexpectancy ~ breastcancerper100th_c', data=sub1).fit()
print (reg1.summary())


# quadratic (polynomial) regression analysis

# run following line of code if you get PatsyError 'ImaginaryUnit' object is not callable
reg2 = smf.ols('lifeexpectancy ~ breastcancerper100th_c + I(breastcancerper100th_c**2)', data=sub1).fit()
print (reg2.summary())


####################################################################################
# EVALUATING MODEL FIT
####################################################################################

# adding alcohol consumption
reg3 = smf.ols('lifeexpectancy ~ breastcancerper100th_c + I(breastcancerper100th_c**2) + breastcancerper100th_c', 
               data=sub1).fit()
print (reg3.summary())


#Q-Q plot for normality
fig4=sm.qqplot(reg3.resid, line='r')

# simple plot of residuals
stdres=pandas.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')


# additional regression diagnostic plots
fig2 = plt.figure(figsize=(12,8))
fig2 = sm.graphics.plot_regress_exog(reg3,  "breastcancerper100th_c", fig=fig2)

# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
print(fig3)


