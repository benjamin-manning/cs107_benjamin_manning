def dna_complement(dna_string):
    if len(dna_string) == 0:
        print('Input must be nonzero in length')
        return
    dna_comp = ''
    for dna in dna_string:
        if dna == 'A':
            dna_comp += 'T'
        elif dna == 'T':
            dna_comp += 'A'
        elif dna == 'G':
            dna_comp += 'C'
        elif dna == 'C':
            dna_comp += 'G'
        else:
            print("Input must only contain A, T, C, G")
            return
    print(dna_comp)
    return dna_comp
dna_complement('AALGC')
