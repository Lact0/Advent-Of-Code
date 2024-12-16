inp = []
with open("b.txt", "r") as file:
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


visited = {(startPos, (0, 1)): 0}
previous = {}
queue = [(startPos, (0, 1))]

while len(queue) > 0:
    pos, dir = queue[0]
    queue = queue[1:]
    key = (pos, dir)
    score = visited[key]

    DIR = [dir, (-dir[1], dir[0]), (dir[1], -dir[0])]
    newScores = [score + 1, score + 1001, score + 1001]

    for i in range(3):
        newDir = DIR[i]
        newScore = newScores[i]
        newPos = (pos[0] + newDir[0], pos[1] + newDir[1])
        if newPos in wallPositions: continue 

        newKey = (newPos, newDir)

        if newKey not in visited.keys():
            visited[newKey] = newScore
            previous[newKey] = [key]
            queue.append(newKey)
        else:
            if newScore == visited[newKey]:
                previous[newKey].append(key)
            if newScore < visited[newKey]:
                previous[newKey] = [key]
                visited[newKey] = newScore
                queue.append(newKey)


mn = 100000000000000000
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
goodDir = []
for dir in DIR:
    key = (endPos, dir)
    if key in visited.keys() and visited[key] < mn:
        mn = visited[key]
        goodDir = [dir]
    elif key in visited.keys() and visited[key] == mn:
        goodDir.append(dir)

print(mn)

vis = set()
vis.add(endPos)
for dir in goodDir:
    cur = [(endPos, dir)]
    while len(cur) > 0:
        newCur = []

        for p, d in cur:
            vis.add(p)
            if (p, d) not in previous.keys(): continue
            prev = previous[(p, d)]
            for newP, newD in prev:
                newCur.append((newP, newD))
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

print(len(vis))

# 12:25 AM