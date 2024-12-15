inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

wallPositions = set()
boxPositions = set()
playerPos = (0, 0)
movements = []
midIndex = 0
for i in range(len(inp)):
    if inp[i] == "":
        midIndex = i
        break
    for j in range(len(inp[i])):
        if inp[i][j] == "#":
            wallPositions.add((j, i))
        if inp[i][j] == "O":
            boxPositions.add((j, i))
        if inp[i][j] == "@":
            playerPos = (j, i)

tr = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}

for i in range(midIndex + 1, len(inp)):
    for m in inp[i]:
        movements.append(tr[m])

def pushBox(pos, dir):
    if pos in wallPositions:
        return False
    if pos not in boxPositions:
        return True

    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    if pushBox(nextPos, dir):
        boxPositions.remove(pos)
        boxPositions.add(nextPos)
        return True
    return False

def printMaze():
    for c in range(len(inp[0])):
        s = ""
        for r in range(midIndex):
            if (r, c) in wallPositions:
                s += "#"
            elif (r, c) in boxPositions:
                s += "0"
            elif (r, c) == playerPos:
                s += "@"
            else:
                s += "."
        print(s)
    print()


# Run through all moves
for move in movements:
    nextPos = (playerPos[0] + move[0], playerPos[1] + move[1])
    if nextPos in wallPositions:
        continue
    if nextPos in boxPositions and not pushBox(nextPos, move):
        continue
    playerPos = nextPos
    # print(move)
    # printMaze()


# Get solution
total = 0
for pos in boxPositions:
    print(pos)
    total +=  pos[0] + 100 * pos[1]
print(total)

# 12:22 AM