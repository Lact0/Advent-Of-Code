inp = []
with open("b.txt", "r") as file:
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
            if not isValid(nI, nJ):
                perim += 1   
                continue
            if inp[nI][nJ] != char:
                perim += 1
                continue
            queue.append((nI, nJ))
    regions.append(seenSet)

    return area, perim


total = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if not any((i, j) in x for x in regions):
            area, perim = calcRegion(i, j)
            total += area * perim


print(total)

# 12:10 AM