#Script to generate graph of expression data 
#Author: Janice
#Date: 12/2/2017
#Last updated: 12/2/2017

#import packages
import pandas as pd 
from plotnine import *

#read in data
data = pd.read_csv("expCountNames", ',')

#Give columns names for easier plotting 
data.columns = ['Mouse',"Protein", "counts"]
#print data 

#initial scatter plot 
p = ggplot(data,aes(x="Protein", y = "counts"))
p + geom_point(data,aes(color='Mouse', na_rm=True)) + theme_classic()

#other try 
a = ggplot(data,aes(x="Protein", y = "counts"))
a +geom_bar(stat='identity', )

#bar plot with Protein on x-axis 
YAY = (ggplot(data, aes(x='Protein', y='counts', fill='Mouse'))
 + geom_bar(stat='identity', position='dodge')) 
 
#bar plot with treatment(Mouse) on x-axis 
what = (ggplot(data, aes(x='Mouse', y='counts', fill='Protein'))
 + geom_bar(stat='identity', position='dodge')) 
