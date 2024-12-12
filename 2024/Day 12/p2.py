inp = []
with open("s5.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

regions = []

def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def calcRegion(startI, startJ):
    char = inp[startI][startJ]
    perim = 0
    area = 0                 
                             
    seenSet = set()

    #Map of (i, j): (di, dj) direction of edge      
    edgeMap = {}
    queue = [(startI, startJ)]
    while len(queue) > 0:    
        
        i, j = queue[0]      
        queue = queue[1:]
        if (i, j) in seenSet: continue

        seenSet.add((i, j)) 
        edgeMap[(i, j)] = set()
        area += 1            

        for di, dj in DIR:   
            nI = i + di      
            nJ = j + dj      

            if not isValid(nI, nJ) or inp[nI][nJ] != char:
                edge = (di, dj)
                edgeMap[(i, j)].add(edge)

                # Look through neighbors to see if this edge is shared
                n1 = (i - dj, j - di)
                n2 = (i + dj, j + di)
                shared = False
                if n1 in edgeMap.keys() and edge in edgeMap[n1]:
                    shared = True
                if n2 in edgeMap.keys() and edge in edgeMap[n2]:
                    shared = True

                if not shared: 
                    perim += 1   
                continue

            queue.append((nI, nJ))

    regions.append(seenSet)
    print(char, area, perim)

    return area, perim


total = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):

        if not any((i, j) in x for x in regions):
            area, perim = calcRegion(i, j)
            total += area * perim


print(total)

# First wrong answer: 821737