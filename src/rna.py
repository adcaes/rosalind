'''
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

with open('rosalind_rna.txt', 'r') as f:
    dna = f.read()
    rna = dna.replace('T', 'U')
    print rna
