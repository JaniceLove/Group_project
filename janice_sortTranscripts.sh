#Date: Nov. 27, 2017 
#Author: Janice Love
#Purpose: To sort transcript results from the BLAST of uniquetranscripts.fasta

#need to rewrite this as a for loop for efficiency 


for line in  $@ 
do
cat "$@" | grep -e 'Transcript_1,' > transcript_1.txt;
cat "$@" | grep -e 'Transcript_10' > transcript_10.txt;
cat "$@" | grep -e 'Transcript_2' > transcript_2.txt;
cat "$@" | grep -e 'Transcript_6' > transcript_6.txt;
cat "$@" | grep -e 'Transcript_8' > transcript_8.txt;
cat "$@" | grep -e 'Transcript_9' > transcript_9.txt;
done 
