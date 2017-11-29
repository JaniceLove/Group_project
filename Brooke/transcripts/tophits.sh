#loop to write the first line (top hit) to a new table
#only works if each of the 6 transcripts are downloaded as separate tables

for file in *.csv  
do
head -1 $file
done > tophits.csv

