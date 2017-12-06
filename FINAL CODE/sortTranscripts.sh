#Date: Nov. 27, 2017 
#Author: Janice Love
#Purpose: To sort transcript results from the BLAST of uniquetranscripts.fasta

#First: split the BLAST results into separate files 

cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_1" > transcript_1.txt
cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_2" > transcript_2.txt
cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_6" > transcript_6.txt
cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_8" > transcript_8.txt
cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_9" > transcript_9.txt
cat 1SD32SM401R-Alignment-HitTable.csv  | grep -w "Transcript_10" > transcript_10.txt

##Sort the transcript files into table with top hits from each transcript file of BLAST results 
#This is in separate folder to be able to use "*" wildcard 
#Each file is sorted by %identity (column 5)  and by E-value (column 13)  
#The top hit is then stored in file called "topHits"  

for file in *.txt;
do
    cat *.txt | sort -k5,5 -k13,13 | head -1 $file  >> topHits
done

#-------------Below is random other code I tried but didn't actually need -----------------------------------------------
#cat transcript_1.txt | sed 'y/";"/" "/' > one.txt # This fixes the formating error: it seems that an extra read separated by ";" is read as "," if you open it in a csv. 
#cat transcript_2.txt | sed 'y/";"/" "/' > two.txt
#cat transcript_6.txt | sed 'y/";"/" "/' > six.txt
#cat transcript_8.txt | sed 'y/";"/" "/' > eight.txt
#cat transcript_9.txt | sed 'y/";"/" "/' > nine.txt
#cat transcript_10.txt | sed 'y/";"/" "/' > ten.txt

#--------sorts each set of results into file for that transcript--------------------
#cat one.txt | sort -k5,5 -k13,13 > sorted1.txt
#cat two.txt | sort -k5,5 -k13,13 > sorted2.txt
#cat six.txt | sort -k5,5 -k13,13 > sorted6.txt
#cat eight.txt | sort -k5,5 -k13,13 > sorted8.txt
#cat nine.txt | sort -k5,5 -k13,13 > sorted9.txt
#cat ten.txt | sort -k5,5 -k13,13 > sorted10.txt

#-------pulls out top aligment per transcript ---------------
#cat sorted1.txt | head -2 > topTranscripts.txt 
#cat sorted2.txt | head -2 >> topTranscripts.txt



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
