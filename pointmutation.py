def pointm(s, t):
    hamming = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming += 1
    return hamming

with open('/Users/shivaniramesh/Desktop/rosalind_hamm.txt') as input_data:
    s = input_data.readline().strip()
    t = input_data.readline().strip()

#s = "AAAACCCGGT"
#t = "GAAACCCGGT"
print(pointm(s, t))