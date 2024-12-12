inp = []
with open("s5.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

used = set()


def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])


DIR = ((-1, 0), (1, 0), (0, 1), (0, -1))
def calcRegion(startI, startJ):
    char = inp[startI][startJ]
    area = 0                 

    # Contains (i, j, di, dj)
    edgesToCheck = []

    seenSet = set()
    queue = [(startI, startJ)]
    while len(queue) > 0:    
        
        i, j = queue[0]      
        queue = queue[1:]
        if (i, j) in seenSet: continue

        seenSet.add((i, j)) 
        area += 1            

        for di, dj in DIR:   
            nI = i + di      
            nJ = j + dj      

            if not isValid(nI, nJ) or inp[nI][nJ] != char:
                edgesToCheck.append((i, j, di, dj))
                continue

            queue.append((nI, nJ))




    # Go through edges and count the copies
    for i in seenSet:
        used.add(i)

    perim = 0
    while len(edgesToCheck) > 0:
        i, j, di, dj = edgesToCheck.pop()
        n1i, n1j = (i - dj, j - di)
        n2i, n2j = (i + dj, j + di)

        hasNeighbors = False
        if (n1i, n1j, di, dj) in edgesToCheck: hasNeighbors = True
        if (n2i, n2j, di, dj) in edgesToCheck: hasNeighbors = True

        if not hasNeighbors: perim += 1

    print(char, area, perim)
    return area * perim


total = 0
for i in range(len(inp)):
    for j in range(len(inp)):
        if (i, j) in used: continue
        total += calcRegion(i, j)
print(total)