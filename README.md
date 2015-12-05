# Multipe Regression Model

GapMinder collects data from a handful of sources, including the Institute for Health Metrics and Evaluation, US Census Bureau's International Database, United Nations Statistics Division and the World Bank

In this occasion I analyse the relation between breastcancerper100th as Explanatory variable and lifeexpectancy as respond variable. Firstly I show the plot of linear regression model.

###Output

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img1.png)


After that I made the polinomial regression using the order equal two to plotting the results. Therefore the best fitting line is curve. We can see that while the breast cancer is increassing the life expectancy is decreassing.

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img2.png)

Centeering is important because it makes it considerably easier t interpret the regression coefficients. The results show that the p value and coeficient estimate that life expectancy is positively associated with breast cancer. The blue linear indicates the R-squeare is 43% indicating that the linear association of breast is capturing 43% of variablility in life expectancy rating

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img3.png)

When I run the polynomial regression the beta value of breast cancer is positive and the p value is less of 0.05. In addition, the quadratic term is negatively insignificant indicating the curvilinear pattern we observed in my scatter plot is statistically significant. Indicates that the curve is concave -from positive to negative value-. In addition the R-squared increases to 0.45. Which means that adding quadratic term for breast cancer, increase the amount of variablility in life expectancy that can be explained by breast cancer from 43% to 45%. Therefore, the best fitting line for this association is that include curvature

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img4.png)

### Adding hivrate

The intercept is the value of the response variable when all explanatory variables are held constant at zero. Therefore the intercept is life expectany at the mean of breast cancer and hiv rate. There is also a show that coefficients for the linear and quadratic variables, remain significant after adjusting for hiv rate. HIV rate is also statistically significant. The negative regression coefficient indicates that countries with a high rate of hiv tend to decreasse life expectancy rate. 

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img5.png)

### Q Q Plot

I can take a look at this residual variability, which helps us to see how large the resiuals are and whether our regression assumptions are met.

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img6.png)

We can see that residuals generally follow a straight line, but deviate at the lower and higher quantiles. This indicates that our residuals did not follow perfect normal distributtion. Other explanatory variables that we might consider including in our model, that could improve estimation of the observer curvilinearity.

The plot that show the interval of 95%. This suggests that the fit of the model is relatively poor and could be improved

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img7.png)

Additional regression diagnostic plots

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img8.png)

Leverage plot

![alt tag](https://github.com/marlonsvl/multipleRegressionModel/blob/master/images/img9.png)




