def dna_complement(dna_string):
    if len(dna_string) == 0:
        print('Input must be nonzero in length')
        return
    dna_comp = ''
    for dna in dna_string:
        if dna == 'A' or dna == 'a':
            dna_comp += 'T'
        elif dna == 'T' or dna == 't':
            dna_comp += 'A'
        elif dna == 'G' or dna == 'g':
            dna_comp += 'C'
        elif dna == 'C' or dna == 'c':
            dna_comp += 'G'
        else:
            print("Input must only contain A, T, C, G")
            return
    return dna_comp

print('Example valid input string is CcTacGAtAGCaCGCgg')
dna_comp = dna_complement('CcTacGAtAGCaCGCgg')
print(f'The complement DNA string is {dna_comp}')
print('Example invalid input string is ACIJVGCT83GGTCA')
inv_dna_comp = dna_complement('ACIJVGCT83GGTCA')
print(inv_dna_comp )

