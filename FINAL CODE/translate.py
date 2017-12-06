#Date: Nov. 28, 2017
#Author: Janice Love
#file for translating amino acids of provided sequences into proteinSequences

#import packages

import re
from sys import argv
script, filename = argv
from itertools import takewhile

##open data files 
#opening files below for translating 

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

def translate_dna(sequence, codonmap_dict, stop_codons = ('TAA', 'TGA', 'TAG')):
    #find first start codon 
    start = sequence.find('ATG')
    
    #trim sequence starting at first start codon 
    trimmed_sequence = sequence[start:]
    
    #split sequence into codons 
    codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence), 3)]
 
 
    coding_sequence = takewhile(lambda x: x not in stop_codons and len(x) == 3 , codons)
    protein_sequence = ''.join([codonmap_dict[codon] for codon in coding_sequence])

    return "{0}_".format(protein_sequence)

#control1 fasta file translation

outfile = open ("ctrl_1_protein", 'w')
for line in open("control1.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translate_dna (sequence, codonmap_dict, stop_codons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

#control 2 fasta file translation

outfile = open ("ctrl_2_protein", 'w')
for line in open("control2.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translate_dna (sequence, codonmap_dict, stop_codons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

#obese 1 fasta file translation

outfile = open ("obese1_protein", 'w')
for line in open("obese1.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translate_dna (sequence, codonmap_dict, stop_codons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

#obese 2 fasta file translation

outfile = open ("obese2_protein", 'w')
for line in open("obese2.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translate_dna (sequence, codonmap_dict, stop_codons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

#close files

codons.close()
