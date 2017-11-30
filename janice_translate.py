#Date: Nov. 28, 2017
#Author: Janice Love
#file for translating amino acids of provided sequences into proteinSequences

#import packages
import re 

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

stop_codons = ['TAA', 'TGA', 'TAG']
stop = re.compile(r'(TAA | TGA | TAG)')

##function to find first ATG, trim the sequence 
#use regex instead?

def trimSeq (sequence, stop):
    #search for first occurence of 'ATG'
    start = sequence.find('ATG')
    
    #Set sequence to start there
    sequencestart = sequence[int(start):]
     
    
    #Search for first stop codon 
    end = stop.match(sequencestart)
    
    
    #stop = sequencestart.find('TAA' or 'TAG' or 'TGA')
    cds = str(sequencestart[:(end)])
    
    # Take sequence from the first start codon
    trimmed_sequence = sequence[start:]
    print trimmed_sequence 

    return trimmed_sequence

def codon_split (trimmed_sequence)
    # Split it into triplets
    codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence), 3)]
    #print(len(codons))
    #print(trimmed_sequence)
    print(codons)
#------------------------------------------------------------------------------------

outfile = open ("ctrl_1_protein", 'w')
for line in ctrl_1:
    line = line.strip()
    if ">" in line:
        outfile.write(line + "\n")
    else:
        sequence = line



trimSeq (sequence, stop)


codons.close()        
ctrl_1.close()
ctrl_2.close()
exp_1.close()
exp_2.close()