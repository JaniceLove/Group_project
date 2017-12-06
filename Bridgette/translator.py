##Translate nucelotides to amino acid sequence

#load packages
import pandas

#load map
map=open("codonmap.txt", "r")

#create dictionary of codon map
codon_dictionary={}
for line in map:
    cols = line.strip()
    cols = line.split()
    if cols[1] in codon_dictionary:
        print("Duplicate: " +cols[1])
        break
    else:
        codon_dictionary[cols[1]] = cols[0]

#load nucleotide sequence to translate as read only
nsequnce = open(" ", "r")

#create document as write only to save results to
translation = open("translationfile.txt", "w")

#define start of sequence by first ATG
start_regex = 


    #variable1 = some kind of search function looking for "ATG'

#define end of sequence
    #variable2 = some kind of search function looking for 'TAA' in variable1
    
#CDS = sequence between variable 1 and variable 2 points

#for loop for 3 nucleotide letters in CDS
    #replace with amino acid letter
    #append to document
    #go to next 3 letters
    
    
    
## from the internet

with open ("dna.txt", "r") as myfile:
    data=myfile.readlines()

DNA=data[1].strip()
start = DNA.find('AUG')
if start!= -1:
    while start+2 < len(DNA):
        codon = DNA[start:start+3]
        if codon == "UAG": break;
        print(map[codon])
        start+=3
    