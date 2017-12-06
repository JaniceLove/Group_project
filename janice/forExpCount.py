#To graph expression data-shell/



##read in file
data = open("finalhmmout.txt", 'r')

ctrl1_T1 = 0
ctrl1_T2 = 0
ctrl1_T3 = 0
ctrl1_T5 = 0


##loop thorough file to count number of hits 
for i in range (0, len(data),1):
    if "Control1" and "transcript1" in line:
        ctrl1_T1 = ctrl1_T1 + 1
    if "Control1" and "transcript2" in line:
        ctrl1_T2 = ctrl1_T2 + 1
    if "Control1" and "transcript3" in line:
        ctrl1_T3 = ctrl1_T3 + 1
    if "Control1" and "transcript5" in line:
        ctrl1_T5 = ctrl1_T5 + 1 
    if "Control2" and "transcript1" in line:
        ctrl2_T1 = add count to list 
    if "Control2" and "transcript2" in line:
        ctrl2_T2 = []
    if "Control2" and "transcript3" in line:
        ctrl2_T3 = add count to line 
    if "Control2" and "transcript5" in line:
        ctrl2_T5 = add count to line 

data.close()