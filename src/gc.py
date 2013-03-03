'''
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''
from collections import Counter
from Bio import SeqIO

max_gc_id = None
max_gc = 0
for record in SeqIO.parse('rosalind_gc.txt', "fasta"):
    c = Counter(record.seq)
    gc = float(c['C'] + c['G'])/float(len(record.seq))
    if gc > max_gc:
        max_gc, max_gc_id = gc, record.id

print max_gc_id
print max_gc*100
