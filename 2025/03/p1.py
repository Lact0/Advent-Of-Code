
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def rowCharge(row):
    ind1 = 0
    max1 = 0
    for i in range(len(row) - 1):
        if int(row[i]) > max1:
            max1 = int(row[i])
            ind1 = i
    
    ind2 = 0
    max2 = 0
    for i in range(ind1 + 1, len(row)):
        if int(row[i]) > max2:
            max2 = int(row[i])
            ind2 = i
    return max1 * 10 + max2

s = 0
for row in inp:
    s += rowCharge(row)
    # print(rowCharge(row))
print(s)
