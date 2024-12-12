inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

regions = []

def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[-1, 0], [0, -1], [1, 0], [0, 1]]
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

        for x in range(4):
            di, dj = DIR[x] 
            nI = i + di      
            nJ = j + dj      

            di2, dj2 = DIR[(x + 1) % 4]
            nI2 = di2 + i
            nJ2 = dj2 + j

            # outie edges
            if not isValid(nI, nJ) or inp[nI][nJ] != char:
                if not isValid(nI2, nJ2) or inp[nI2][nJ2] != char:
                    perim += 1

                continue

            ni3 = nI + di2
            nj3 = nJ + dj2

            if isValid(nI2, nJ2) and inp[nI2][nJ2] == char:
                if inp[ni3][nj3] != char:
                    perim += 1

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
# 1:05 AM