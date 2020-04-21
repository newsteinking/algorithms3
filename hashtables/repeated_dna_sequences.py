'''
All DNA is composed of a series of nucleotides abbreviated as 
A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes 
useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

def repeated_dna(dna):
    if len(dna) < 10: return []

    result, seen = set(), set()
    for i in range(len(dna)-9):
        if dna[i:i+10] in seen:
            result.add(dna[i:i+10])
        else:
            seen.add(dna[i:i+10])
    return result
