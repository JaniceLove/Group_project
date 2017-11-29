def DNA_to_protein (sequence):
    proteinsequence = ''
    start = sequence.find('ATG')
    sequencestart = sequence[int(start):]
    stop = sequencestart.find('TAA' or 'TAG' or 'TGA')
    cds = str(sequencestart[:int(stop)+3])

    for n in range(0,len(cds),3):
        if cds[n:n+3] in dict:
            proteinsequence += dict[cds[n:n+3]]
            print proteinsequence
        sequence = ''
        
    return proteinsequence 


header = ''
sequence = ''
for line in ctrl_1:
    if line[0] == ">":
        if header != '':
            print header
            DNA_to_protein(sequence)

        header = line.strip()
        sequence = ''
    else:
        sequence += line.strip()

print header 
DNA_to_protein(sequence)