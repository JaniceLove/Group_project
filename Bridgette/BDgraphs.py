##Generating a plot

#Load packages
import numpy
import pandas
from plotnine import *

#Load file
hmmfile=pandas.read_csv("finalhmmout.txt", header=0, sep=" ")

#Generate bar graph that summarizes means of data
d=ggplot(hmmfile)+theme_classic()+xlab("Treatment")+ylab("Expression_Levels")
d+geom_bar(aes(x="factor(feed)",y="weight"),stat="summary",fun_y=numpy.mean)

+#plot for population curves
 +rates=ggplot(store_rs,aes(x="time",y="N"))+theme_classic()
 +
 +#add each population to the graph
 +rates=rates+geom_line(store_rs,aes(y="r1"))
 +rates=rates+geom_line(store_rs,aes(y="r2"))
 +rates=rates+geom_line(store_rs,aes(y="r3"))
 +rates=rates+geom_line(store_rs,aes(y="r4"))


