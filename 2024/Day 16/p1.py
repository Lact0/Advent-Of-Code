inp = []
with open("s.txt", "r") as file:
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
previous = {}

# Contains (position, dir)
queue = [(startPos, (0, 1))]

while len(queue) > 0:
    pos, dir = queue[0]
    queue = queue[1:]
    score = visited[pos]
    # print(pos)

    fNext = (pos[0] + dir[0], pos[1] + dir[1])
    newScore = score + 1
    if fNext not in wallPositions:
        if fNext not in visited.keys():
            queue.append((fNext, dir))
            previous[fNext] = pos
            visited[fNext] = newScore
        else:
            if visited[fNext] > newScore:
                visited[fNext] = newScore
                previous[fNext] = pos
                queue.append((fNext, dir))
    
    lNext = (pos[0] - dir[1], pos[1] + dir[0])
    newScore = score + 1001
    if lNext not in wallPositions:
        if lNext not in visited.keys():
            queue.append((lNext, (-dir[1], dir[0])))
            previous[lNext] = pos
            visited[lNext] = newScore
        else:
            if visited[lNext] > newScore:
                visited[lNext] = newScore
                previous[lNext] = pos
                queue.append((lNext, (-dir[1], dir[0])))

    rNext = (pos[0] + dir[1], pos[1] - dir[0])
    newScore = score + 1001
    if rNext not in wallPositions:
        if rNext not in visited.keys():
            queue.append((rNext, (dir[1], -dir[0])))
            previous[rNext] = pos
            visited[rNext] = newScore
        else:
            if visited[rNext] > newScore:
                previous[rNext] = pos
                visited[rNext] = newScore
                queue.append((rNext, (dir[1], -dir[0])))
    # print(queue)
    # print(visited)

# cur = endPos
# while cur != startPos:
#     print(cur, visited[cur])
#     cur = previous[cur]





print(visited[endPos])

# 12:25 AM