#Date: Nov. 27, 2017 
#Author: Janice Love
#Purpose: To sort transcript results from the BLAST of uniquetranscripts.fasta

#need to rewrite this as a for loop for efficiency 


cat 1SE3G42N01R-Alignment.txt | grep -w "Transcript_1" > transcript_1.txt #this searches for only 1, instead of getting both 1 and 10
cat transcript_1.txt | sed 'y/";"/" "/' > one.txt # This fixes the formating error: it seems that an extra read separated by ";" is read as "," if you open it in a csv. 
 










#------------------------------------------------------------------
#for line in  $@ 
#do
#cat "$@" | grep -e 'Transcript_1,' > transcript_1.txt;
#cat "$@" | grep -e 'Transcript_10' > transcript_10.txt;
#cat "$@" | grep -e 'Transcript_2' > transcript_2.txt;
#cat "$@" | grep -e 'Transcript_6' > transcript_6.txt;
#cat "$@" | grep -e 'Transcript_8' > transcript_8.txt;
#cat "$@" | grep -e 'Transcript_9' > transcript_9.txt;
#done 
