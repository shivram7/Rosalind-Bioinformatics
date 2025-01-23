def revcomp(s):
    comp = {
        "A" : "T", 
        "T" : "A",
        "G" : "C",
        "C" : "G"
    }
    rev = s[::-1]
    #print(rev)
    rc = "".join(comp[x] for x in rev)
    return rc

with open('/Users/shivaniramesh/Desktop/rosalind_revc.txt') as input_data:
    s = input_data.read().strip()

#s = "AAAACCCGGT"
print(revcomp(s))