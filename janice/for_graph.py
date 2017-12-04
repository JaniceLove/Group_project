#Script to generate graph of expression data 
#Author: Janice
#Date: 12/2/2017
#Last updated: 12/2/2017

#import packages
import pandas as pd 
from plotnine import *

data = pd.read_csv("expression_counts", delimiter=",")

ctrl1=0
ctrl2=0
obese1=0
obese2=0

for i in  range (0, len(data),1):
    if data.Data[i] == "ctrl1_T1":
        ctrl1 = ctrl1 + data.expressioncount[i]
##graph expression levels across the two ctrl and two obese datasets 
#graph by transcript?
T1_ctrl = 0
T1_obese = 0

