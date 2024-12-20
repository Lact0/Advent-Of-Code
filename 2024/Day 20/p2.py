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
        if inp[i][j] == "E":
            endPos = (i, j)
        if inp[i][j] == ".":
            openPositions.add((i, j))

        
def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# Get distance to the end in all elements
queue = [(endPos, 0)]
dist = {}
visited = set()
while len(queue) > 0:
    pos, steps = queue[0]
    queue = queue[1:]

    if pos in visited: continue
    visited.add(pos)
    dist[pos] = steps


    for dir in DIR:
        newX = pos[0] + dir[0]
        newY = pos[1] + dir[1]
        if isValid(newX, newY) and (newX, newY) not in wallPositions:
            queue.append(((newX, newY), steps + 1))


# Go through path and simulate glitches
glitches = {}
maxGlitchDist = 20

queue = [(startPos, 0)]
visited = set()
while len(queue) > 0:
    pos, steps = queue[0]
    queue = queue[1:]
    if pos in visited: continue
    visited.add(pos)

    if steps % 100 == 0: print(steps)

    # Simulate all glitches from this position
    for dest in openPositions:
        distance = abs(dest[0] - pos[0]) + abs(dest[1] - pos[1])
        if distance > maxGlitchDist: continue

        totalTime = distance + dist[dest]
        dt = dist[pos] - totalTime
        if dt > 0:
            if dt in glitches:
                glitches[dt] += 1
            else:
                glitches[dt] = 1
    
    for dir in DIR:
        newX = pos[0] + dir[0]
        newY = pos[1] + dir[1]
        if isValid(newX, newY) and (newX, newY) not in wallPositions:
            queue.append(((newX, newY), steps + 1))

print(glitches)
total = 0
for key in glitches:
    if key >= 100:
        print(key, glitches[key])
        total += glitches[key] + 1
print(total)

# 992872, 994960 - NO
# S SHOULD BE 285