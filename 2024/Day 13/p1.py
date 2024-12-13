inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

#Problem is (ax + ay j, bx + byj, tx + tyj)
problems = []
for i in range((len(inp) - 1) // 4):
    l1 = inp[i*4]
    l2 = inp[i*4+1]
    l3 = inp[i*4+2]

    ax = int(l1[l1.index("X")+1:l1.index(",")]) 
    ay = int(l1[l1.index("Y")+1:])

    bx = int(l2[l2.index("X")+1:l2.index(",")]) 
    by = int(l2[l2.index("Y")+1:])

    ex = int(l3[l3.index("X")+2:l3.index(",")]) 
    ey = int(l3[l3.index("Y")+2:])

    problems.append((ax + ay * 1j, bx + by * 1j, ex + ey * 1j))

def getTokens(a, b, target):
    # print(a, b, target)
    for numA in range(100):
        for numB in range(100):
            final = a * numA + b * numB
 
            if final == target:
                return numA * 3 + numB
            
    return 0
            


print(len(problems))
total = 0
for a, b, target in problems:
    total+= getTokens(a, b, target)
print(total)

# 12:17 AM