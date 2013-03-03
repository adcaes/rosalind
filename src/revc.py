'''
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

with open('rosalind_revc.txt', 'r') as f:
    dna = f.read().strip()
    rev = reversed(dna)
    revc = []
    for b in rev:
        revc.append(complements[b])

    print ''.join(revc)
