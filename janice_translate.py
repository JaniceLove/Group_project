#Date: Nov. 28, 2017
#Author: Janice Love
#file for translating amino acids of provided sequences into proteinSequences

#open data files 
ctrl_1 = open ("control1.fasta", 'r')
ctrl_2 = open ("control2.fasta", 'r')
exp_1 = open ("obese1.fasta", 'r')
exp_2 = open ("obese2.fasta", 'r')

codons = open ("codonmap.txt", 'r')

#create a dictionary for codon map 
dict = {}

#reverse col 0 and 1 to create full dictionary. (compared to dict code from tut8)
for line in codons:
    line = line.strip()
    cols = line.split()
    if cols[1] in dict:
        print ("Duplicate: " + dict [0])
        break
    else:
        dict [cols[1]] = cols[0]

stop_codons = ('TAA', 'TGA', 'TAG')
#find first start codon in sequences provided------------------------------------------------------- 
from itertools import takewhile

def DNA_to_protein (sequence, dict, stop_codons):       
    start = sequence.find('ATG')

    # Take sequence from the first start codon
    trimmed_sequence = sequence[start:]

    # Split it into triplets
    codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence), 3)]
    print(len(codons))
    print(trimmed_sequence)
    print(codons)

    # Take all codons until first stop codon
    coding_sequence  =  takewhile(lambda x: x not in stop_codons and len(x) == 3 , codons)

    # Translate and join into string
    protein_sequence = ''.join([dict[codon] for codon in coding_sequence])

    # This line assumes there is always stop codon in the sequence
    return "{0}_".format(protein_sequence)
#-------------------------------------------------------------------------------------------
outfile = open("ctrl_1_protein", 'w')

header = 'header'
sequence = 'sequence'
for line in ctrl_1:
    line = line.strip()
    if ">" in line:
        outfile.write(line + "\n")
        DNA_to_protein(sequence, dict, stop_codons)
    else:
        sequence += line.strip()

print header 
DNA_to_protein(sequence, dict, stop_codons)





codons.close()        
ctrl_1.close()
ctrl_2.close()
exp_1.close()
exp_2.close()