def trans(t):
    tl = [n for n in t]
    u = []
    for i in range(len(tl)):
        if tl[i] =="T":
            u.append("U")
        else: 
            u.append(tl[i])
    return "".join(u)

with open('/Users/shivaniramesh/Desktop/rosalind_rna.txt') as input_data:
    t = input_data.read().strip()

print(trans(t))