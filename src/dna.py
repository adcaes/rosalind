'''
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

from collections import Counter

with open('rosalind_dna.txt', 'r') as f:
    dna = f.read()
    dna = Counter(dna)
    for base in ['A', 'C', 'G', 'T']:
        print str(dna[base]) + ' ',
