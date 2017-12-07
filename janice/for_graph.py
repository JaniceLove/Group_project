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


p = ggplot(data,aes(x="Protein", y = "counts"))
p + geom_point(data,aes(color='Mouse', na_rm=True)) + theme_classic()


