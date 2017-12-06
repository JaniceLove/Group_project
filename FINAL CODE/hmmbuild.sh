#converting reference files (*.ref) into muscle files

./muscle3.8.31_i86win32.exe -in T1_GSTprotSeq.fasta -out transcript1.ref.muscle
./muscle3.8.31_i86win32.exe -in T2_synaptoporin_protSeq.fasta -out transcript2.ref.muscle
./muscle3.8.31_i86win32.exe -in T3_slc7a12protSeq.fasta -out transcript3.ref.muscle
./muscle3.8.31_i86win32.exe -in T4_ptpn5_protSeq.fasta -out transcript4.ref.muscle
./muscle3.8.31_i86win32.exe -in T5_atp12a_protSeq.fasta -out transcript5.ref.muscle
./muscle3.8.31_i86win32.exe -in T6_lhx2_protSeq.fasta -out transcript6.ref.muscle



#creating an hmmbuild for each reference file

hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript1.ref.hmm transcript1.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript2.ref.hmm transcript2.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript3.ref.hmm transcript3.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript4.ref.hmm transcript4.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript5.ref.hmm transcript5.ref.muscle
hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe transcript6.ref.hmm transcript6.ref.muscle

#loop to compare .fasta files (RNA-seq data) to each reference file (6 transcripts)
#i = variable = filename (translated RNA-seq files)
for i in *_protein
do
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript1.hits transcript1.ref.hmm $i
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript2.hits transcript2.ref.hmm $i
        hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript3.hits transcript3.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript4.hits transcript4.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript5.hits transcript5.ref.hmm $i
	hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.transcript6.hits transcript6.ref.hmm $i
done


#in any .hits file output results to file called finalhmmout.txt

cat *.hits >> finalhmmout.txt


