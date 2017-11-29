#converting reference files (*.ref) into muscle files

./muscle3.8.31_i86win32.exe -in transcript1.ref -out transcript1.ref.muscle
./muscle3.8.31_i86win32.exe -in transcript2.ref -out transcript2.ref.muscle
./muscle3.8.31_i86win32.exe -in transcript3.ref -out transcript3.ref.muscle
./muscle3.8.31_i86win32.exe -in transcript4.ref -out transcript4.ref.muscle
./muscle3.8.31_i86win32.exe -in transcript5.ref -out transcript5.ref.muscle
./muscle3.8.31_i86win32.exe -in transcript6.ref -out transcript6.ref.muscle



#creating an hmmbuild for each reference file

hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript1.ref.hmm transcript1.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript2.ref.hmm transcript2.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript3.ref.hmm transcript3.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript4.ref.hmm transcript4.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript5.ref.hmm transcript5.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript6.ref.hmm transcript6.ref.muscle

#loop to compare .fasta files (RNA-seq data) to each reference file (6 transcripts)
#i = variable = filename (translated RNA-seq files)
for i in *fasta
do
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript1.hits transcript1.ref.hmm $i
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript2.hits transcript2.ref.hmm $i
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript3.hits transcript3.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript4.hits transcript4.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript5.hits transcript5.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript6.hits transcript6.ref.hmm $i
done


#in any .hits file output results to file called finalhmmout.txt

cat *.hits > finalhmmout.txt


