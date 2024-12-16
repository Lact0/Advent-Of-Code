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

queue = [(startPos, (0, 1), 0, set())]
paths = {}
currentPath = ()
while len(queue) > 0:
    pos, dir, score, visited = queue.pop()
    if pos in wallPositions: continue
    if pos in visited: continue

    currentPath += (pos)
    if pos == endPos:
        paths[currentPath] = score
        currentPath = currentPath[:-1]

    visited.add(pos)

    queue.append(((pos[0] - dir[1], pos[1] + dir[0]), (-dir[1], dir[0]), score + 1001, visited.copy()))
    queue.append(((pos[0] + dir[1], pos[1] - dir[0]), (dir[1], -dir[0]), score + 1001, visited.copy()))
    queue.append(((pos[0] + dir[0], pos[1] + dir[1]), dir, score + 1, visited.copy()))



# for i in range(len(inp)):
#     s = ""
#     for j in range(len(inp[i])):
#         if (i, j) in wallPositions:
#             s += "#"
#         else:
#             s += "."
#     print(s)

min = 1000000000000000000000
for path in paths:
    if paths[path] < min:
        min = paths[path]
print(min)