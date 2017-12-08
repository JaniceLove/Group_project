##Working code

#Load packages
import numpy as np
from plotnine import *

#Load file

hmmfile=pandas.read_csv("expression_counts", header=0, sep=",")

#dodge plot

(ggplot(hmmfile) + 
  aes(x='treatment', y='counts', fill='transcript') +
  geom_bar(stat='identity', position = 'dodge'))

##########All other attempts##########################

#Load packages
import numpy as np
import matplotlib.pyplot as plt

#Load file

#hmmfile=pandas.read_csv("expression_counts", header=0, sep=",")
n_groups = 4
Tran1 = (12, 20, 2, 1)
Tran2 = (15, 20, 100, 93)
Tran3 = (12, 20, 16, 15)
#T4 = 0,0,0,0
#T5 = 18,20,38,38
#T6 = 0,0,0,0

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, Tran1, bar_width, color='b', label='Transcript1')
rects2 = plt.bar(index, Tran2, bar_width, color='g', label='Transcript2')
rects3 = plt.bar(index, Tran3, bar_width, color='orange', label='Transcript3')
#plt.bar(index, T6, bar_width, color='pink', label='Transcript6')
 
plt.xlabel('Treatment')
plt.ylabel('Counts_of_expression')
plt.title('Expression')
plt.xticks(index + bar_width, ('Ctrl1', 'Ctrl2', 'Obese1', 'Obese2'))
plt.legend()
 
plt.tight_layout()
plt.show()

###Attempt2

#Load packages
import numpy as np
import matplotlib.pyplot as plt
import pandas

#Load file

hmmfile=pandas.read_csv("expression_counts", header=0, sep=",")
T1 = hmmfile[hmmfile.transcript == 'T1']
T1 = numpy.loadtxt(Transcript1.counts)
T2 = 15,20,100,93
#Transcript3 = hmmfile[hmmfile.transcript == 'T3']
#T3 = Transcript3.counts
#Transcript4 = hmmfile[hmmfile.transcript == 'T4']
#T4 = Transcript4.counts
#Transcript5 = hmmfile[hmmfile.transcript == 'T5']
#T5 = Transcript5.counts
#Transcript6 = hmmfile[hmmfile.transcript == 'T6']
#T6 = Transcript6.counts


#define number of groups for graph
n_groups = 4

# create plot

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
 
plt.bar(index, T1, bar_width, color='purple', label='Transcript1')
plt.bar(index, T2, bar_width, color='aqua', label='Transcript2')
#plt.bar(index, T3, bar_width, color='lime', label='Transcript3')
#plt.bar(index, T4, bar_width, color='yellow', label='Transcript4')
#plt.bar(index, T5, bar_width, color='orange', label='Transcript5')
#plt.bar(index, T6, bar_width, color='pink', label='Transcript6')
 
plt.xlabel('Treatment')
plt.ylabel('Expression')
plt.title('Expression')
plt.xticks(index + bar_width, ('Ctrl1', 'Ctrl2', 'Obese1', 'Obese2'))
plt.legend()
 
plt.tight_layout()
plt.show()

###Attempt3 with subsetting

#Load packages
import numpy as np
import matplotlib.pyplot as plt
import pandas

#Load file

hmmfile=pandas.read_csv("expression_counts", header=0, sep=",")
Transcript1 = hmmfile[hmmfile.transcript == 'T1']
T1 = Transcript1.counts
T2 = 15,20,100,93
Transcript3 = hmmfile[hmmfile.transcript == 'T3']
T3 = Transcript3.counts
Transcript4 = hmmfile[hmmfile.transcript == 'T4']
T4 = Transcript4.counts
Transcript5 = hmmfile[hmmfile.transcript == 'T5']
T5 = Transcript5.counts
Transcript6 = hmmfile[hmmfile.transcript == 'T6']
T6 = Transcript6.counts


#define number of groups for graph
n_groups = 4

# create plot

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.8
 
plt.bar(index,T1, bar_width, color='purple', label='Transcript1')
 
plt.bar(index,T2, bar_width,
                 alpha=opacity,
                 color='aqua',
                 label='Transcript2')

plt.bar(index,T3, bar_width,
                 alpha=opacity,
                 color='lime',
                 label='Transcript3')
                 
plt.bar(index,T4, bar_width,
                 alpha=opacity,
                 color='yellow',
                 label='Transcript4')
                 
plt.bar(index,T5, bar_width,
                 alpha=opacity,
                 color='orange',
                 label='Transcript5')
                 
plt.bar(index,T6, bar_width,
                 alpha=opacity,
                 color='pink',
                 label='Transcript6')
 
plt.xlabel('Treatment')
plt.ylabel('Expression')
plt.title('Expression')
plt.xticks(index + bar_width, ('Ctrl1', 'Ctrl2', 'Obese1', 'Obese2'))
plt.legend()
 
plt.tight_layout()
plt.show()








