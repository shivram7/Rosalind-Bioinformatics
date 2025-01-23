def nuc_count( dna):
    counts = []
    for x in "ACGT":
        counts.append(str(dna.count(x)))
    #print(counts)
    return " ".join(counts)

with open('/Users/shivaniramesh/Desktop/rosalind_dna.txt') as input_data:
    dna = input_data.read().strip()

print(nuc_count(dna))


    