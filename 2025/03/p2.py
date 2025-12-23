
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def rowCharge(row):
    n = 0
    oldInd = -1
    for i in range(12):
        max = 0
        ind = oldInd
        for j in range(oldInd + 1, len(row) - 11 + i):
            if int(row[j]) > max:
                max = int(row[j])
                ind = j
        oldInd = ind
        n = n * 10 + max
    
    return n

s = 0
for row in inp:
    s += rowCharge(row)
print(s)
