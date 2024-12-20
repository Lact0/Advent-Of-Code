inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))


wallPositions = set()
openPositions = set()
startPos = ()
endPos = ()
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "#":
            wallPositions.add((i, j))
        if inp[i][j] == "S":
            startPos = (i, j)
            openPositions.add((i, j))
        if inp[i][j] == "E":
            endPos = (i, j)
            openPositions.add((i, j))
        if inp[i][j] == ".":
            openPositions.add((i, j))

        
def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# Get times of all positions from end
endDist = {}
queue = [(endPos, 0)]
visited = set()
while len(queue) > 0:
    pos, time = queue[0]
    queue = queue[1:]

    visited.add(pos)
    endDist[pos] = time

    for dir in DIR:
        newPos = (pos[0] + dir[0], pos[1] + dir[1])

        if newPos in openPositions and newPos not in visited:
            queue.append((newPos, time + 1))

totalTime = endDist[startPos]
maxGlitchDist = 20
cutoffDist = 100

# Go thorugh all pairs
glitches = {}
i = 0
for start in openPositions:
    print(i)
    for dest in openPositions:

        dist = abs(start[0] - dest[0]) + abs(start[1] - dest[1])
        if dist > maxGlitchDist: continue
        newTime = (totalTime - endDist[start]) + dist + endDist[dest]
        dt = totalTime - newTime

        if dt > 0:
            if dt in glitches:
                glitches[dt] += 1
            else:
                glitches[dt] = 1
    i += 1

print(glitches)
total = 0
for key in glitches:
    if key >= cutoffDist:
        print(key, glitches[key])
        total += glitches[key]
print(total)