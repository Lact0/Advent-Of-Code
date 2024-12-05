from collections import queue

inp = []
with open("Day 9/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

key = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, -1], [0, 1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[0, -1], [-1, 0]],
    "7": [[0, -1], [1, 0]],
    "F": [[0, 1], [1, 0]],
    ".": [],
    "S": []
}

start = []
for r in range(len(inp)):
    for c in range(len(inp[r])):
        if inp[r][c] == "S":
            start = [r, c]

seen = set(start)
q = queue()

for dr in range(-1, 2, 1):
    for dc in range(-1, 2, 1):
        if dr == 0 and dc == 0:
            continue
        dir = key[inp[start[0] + dr][start[1] + dc]]
        if [-dr, -dc] in dir:
            seen.add([start[0] + dr, start[1] + dc])
            q.append([start[0] + dr, start[1] + dc])

while q:
    pos = q.pop(0)
     