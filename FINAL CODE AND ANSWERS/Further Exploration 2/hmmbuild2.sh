#orcas and turtles rule the world!
#converting reference files (*.ref) into muscle files

./muscle3.8.31_i86win32.exe -in atp12a_turtles.fasta -out atp12a.ref.muscle
./muscle3.8.31_i86win32.exe -in synpr_orca.fasta -out synpr.ref.muscle



#creating an hmmbuild for each reference file

hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe atp12a.ref.hmm atp12a.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe synpr.ref.hmm synpr.ref.muscle


#loop to compare .fasta files (RNA-seq data) to each reference file (6 transcripts)
#i = variable = filename (translated RNA-seq files)
for i in *_protein
do
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.atp12a.hits atp12a.ref.hmm $i
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.synpr.hits synpr.ref.hmm $i
	
done


#in any .hits file output results to file called finalhmmout.txt

cat *.hits >> finalhmmout2.txt









