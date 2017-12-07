#Import packages
import numpy
import pandas
import scipy
from plotnine import *

#assign results.csv to variable named dataframe 
dataframe=pandas.read_csv("results.csv",header=0, sep=",")

#control1plot
ggplot(dataframe, aes(x='transcript', fill='transcript', y='control1')) + geom_bar(stat='identity')

#control2plot
ggplot(dataframe, aes(x='transcript', fill='transcript', y='control2')) + geom_bar(stat='identity')

#obese1plot
ggplot(dataframe, aes(x='transcript', fill='transcript', y='obese1')) + geom_bar(stat='identity')

#obese2plot
ggplot(dataframe, aes(x='transcript', fill='transcript', y='obese2')) + geom_bar(stat='identity')






