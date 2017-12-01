#Date: Nov. 28, 2017
#Author: Janice Love
#file for translating amino acids of provided sequences into proteinSequences

#import packages
import re 
import pandas as pd 

#open data files 
ctrl_1 = open ("control1.fasta", 'r')
ctrl_2 = open ("control2.fasta", 'r')
exp_1 = open ("obese1.fasta", 'r')
exp_2 = open ("obese2.fasta", 'r')

codons = open ("codonmap.txt", 'r')

##create a dictionary for codon map 
codonmap_dict = {}

#for loop to read codonmap.txt into dictionary 
#reverse col 0 and 1 to create full dictionary. (compared to dict code from tut8)
for line in codons:
    line = line.strip()
    cols = line.split()
    if cols[1] in codonmap_dict:
        print ("Duplicate: " + codonmap_dict [0])
        break
    else:
        codonmap_dict [cols[1]] = cols[0]

#stop_codons = ['TAA', 'TGA', 'TAG']
#stop = re.compile(r'(TAA | TGA | TAG)')

##function to read fasta file 
#def read_fasta (file):


sequence = []
for line in ctrl_1:
    line = line.strip()
    if ">" in line: 
        sequence.append (line)

##function to find first start codon 
sequence = sequenceStart.find('ATG')

##function to search for stop codon: tried a variety of these, but can't get them to work. Why?? 
stop = sequenceStart.match(r'TAA | TAG | TGA') #re.compile first, then search as object? OR re.search? 


stop = re.compile (r'TAA|TAG|TGA')
end = stop.match(sequenceStart)

#function to define cds (coding sequence)
cds = str(sequenceStart[:(end)])

##translate cds to protein sequence using codonmap_dict 
#split cds sequence into codons 
codons = [cds[i:i+3] for i in range(0, len(trimmed_sequence), 3)]

##save the translated protein sequences to files 



codons.close()        
ctrl_1.close()
ctrl_2.close()
exp_1.close()
exp_2.close()