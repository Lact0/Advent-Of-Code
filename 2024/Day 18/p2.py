inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [[int(x) for x in i.split(",")] for i in inp]
memorySize = 71
nFallen = 1024


DIR = ((-1, 0), (1, 0), (0, 1), (0, -1))
def isValid(i, j):
    return i >= 0 and j >= 0 and i < memorySize and j < memorySize

startPos = (0, 0)
endPos = (memorySize - 1, memorySize - 1)

# Entry is (pos, steps)
for i in range(nFallen, len(inp)):

    print(i, len(inp))

    ob = set([tuple(inp[i]) for i in range(i)])
    pathExists = False

    queue = [(startPos, 0)]
    visited = set()
    while len(queue) > 0:
        pos, steps = queue[0]
        queue = queue[1:]
        # found exit
        if pos == endPos:
            pathExists = True
            break

        if pos in visited: continue
        visited.add(pos)

        for dir in DIR:
            newX = pos[0] + dir[0]
            newY = pos[1] + dir[1]
            if ((newX, newY) in ob) or not isValid(newX, newY): continue
            queue.append(((newX, newY), steps + 1))
    
    if not pathExists:
        print(i, inp[i-1])
        break

# 12:15 AM