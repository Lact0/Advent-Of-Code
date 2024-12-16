inp = []
with open("mys.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

wallPositions = set()
startPos = ()
endPos = ()
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "#":
            wallPositions.add((i, j))
        if inp[i][j] == "S":
            startPos = (i, j)
        if inp[i][j] == "E":
            endPos = (i, j)

DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

# Contains (i, j): lowestScoreToReach
visited = {startPos: 0}

# Contains pos: [] for everything that has an equal path to it
previous = {startPos: []}

# Contains (position, dir)
queue = [(startPos, (0, 1))]

def getMin(q):
    minInd = 0
    for i in range(len(q)):
        if visited[q[i][0]] < visited[q[minInd][0]]:
            minInd = i
    return minInd


while len(queue) > 0:
    minIndex = getMin(queue)
    pos, dir = queue[minIndex]
    queue = queue[:minIndex] + queue[minIndex + 1:]
    score = visited[pos]


    fNext = (pos[0] + dir[0], pos[1] + dir[1])
    newScore = score + 1
    if fNext not in wallPositions:
        if fNext not in visited.keys():
            queue.append((fNext, dir))
            previous[fNext] = [pos]
            visited[fNext] = newScore
        else:
            if visited[fNext] == newScore:
                previous[fNext].append(pos)
                queue.append((fNext, dir))
            if visited[fNext] > newScore:
                visited[fNext] = newScore
                previous[fNext] = [pos]
                queue.append((fNext, dir))

    lNext = (pos[0] - dir[1], pos[1] + dir[0])
    newScore = score + 1001
    if lNext not in wallPositions:
        if lNext not in visited.keys():
            queue.append((lNext, (-dir[1], dir[0])))
            previous[lNext] = [pos]
            visited[lNext] = newScore
        else:
            if visited[lNext] == newScore:
                previous[lNext].append(pos)
                queue.append((lNext, (-dir[1], dir[0])))
            if visited[lNext] > newScore:
                visited[lNext] = newScore
                previous[lNext] = [pos]
                queue.append((lNext, (-dir[1], dir[0])))

    rNext = (pos[0] + dir[1], pos[1] - dir[0])
    newScore = score + 1001
    if rNext not in wallPositions:
        if rNext not in visited.keys():
            queue.append((rNext, (dir[1], -dir[0])))
            previous[rNext] = [pos]
            visited[rNext] = newScore
        else:
            if visited[rNext] == newScore:
                previous[rNext].append(pos)
                queue.append((rNext, (dir[1], -dir[0])))
            if visited[rNext] > newScore:
                previous[rNext] = [pos]
                visited[rNext] = newScore
                queue.append((rNext, (dir[1], -dir[0])))


    check = (3, 4)
    if fNext == check or lNext == check or rNext == check:
        print(pos, dir, score)

cur = [endPos]
vis = set([endPos])
while len(cur) > 0:
    newCur = []
    for p in cur:
        newPositions = previous[p]
        for newPos in newPositions:
            if newPos not in vis:
                vis.add(newPos)
                newCur.append(newPos)
    cur = newCur

for i in range(len(inp)):
    s = ""
    for j in range(len(inp[i])):
        if (i, j) in wallPositions:
            s += "#"
        elif (i, j) in vis:
            s += "O"
        else:
            s += "."
    print(s)


print(vis)
print(len(vis))
print(visited[endPos])

# 12:25 AM