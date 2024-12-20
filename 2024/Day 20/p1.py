inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

wallPositions = set()
startPos = ()
endPos = ()
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "#":
            wallPositions.add((i, j))
        if inp[i][j] == "S":
            startPos = (i, j)
        if inp[i][j] == "E":
            endPos = (i, j)

        
def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# Find normal best path
bestSteps = 0
queue = [(startPos, 0)]
visited = set()
while len(queue) > 0:
    pos, steps = queue[0]
    queue = queue[1:]

    if pos in visited: continue
    visited.add(pos)

    if pos == endPos:
        bestSteps = steps
        break


    for dir in DIR:
        newX = pos[0] + dir[0]
        newY = pos[1] + dir[1]
        if isValid(newX, newY) and (newX, newY) not in wallPositions:
            queue.append(((newX, newY), steps + 1))



# timeSaved, count
glitches = {}
memo = {}

# Go through the maze again, but try glitching every time
queue = [(startPos, 0)]
visited = set()
while len(queue) > 0:
    pos, steps = queue[0]
    queue = queue[1:]

    if steps % 100 == 0:
        print(steps)

    if pos == endPos: break
    if pos in visited: continue
    visited.add(pos)

    for dir in DIR:
        newX = pos[0] + dir[0]
        newY = pos[1] + dir[1]
        if not isValid(newX, newY): continue

        # Normal path, continue on
        if (newX, newY) not in wallPositions:
            queue.append(((newX, newY), steps + 1))
            continue

        # Try glitching through
        newX = pos[0] + dir[0] * 2
        newY = pos[1] + dir[1] * 2

        if (newX, newY) in wallPositions: continue
        if (newX, newY) in memo:
            dt = memo[(newX, newY)] - bestSteps
            if dt > 0:
                if dt in glitches:
                    glitches[dt] += 1
                else:
                    glitches[dt] = 1
        
        bestTime = 0
        newQueue = [((newX, newY), steps + 2)]
        newVisited = visited.copy()
        while len(newQueue) > 0:
            newPos, newTime = newQueue[0]
            newQueue = newQueue[1:]

            if newPos in newVisited: continue
            newVisited.add(newPos)

            if newPos == endPos:
                bestTime = newTime
                break
            
            for newDir in DIR:
                nNewX = newPos[0] + newDir[0]
                nNewY = newPos[1] + newDir[1]
                if isValid(nNewX, nNewY) and (nNewX, nNewY) not in wallPositions:
                    newQueue.append(((nNewX, nNewY), newTime + 1))

        memo[(newX, newY)] = bestTime
        if bestTime != 0 and (dt := bestSteps - bestTime) > 0:
            
            if dt in glitches:
                glitches[dt] += 1
            else:
                glitches[dt] = 1

print(glitches)

total = 0
for key in glitches:
    if key >= 100:
        total += glitches[key]
print(total)

# 12:42 AM
# I am disgusted by my code, and I already know ten ways to make this easier and faster.