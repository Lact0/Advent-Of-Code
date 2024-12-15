inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

wallPositions = set()
boxPositions = set()
boxJoints = {}
playerPos = (0, 0)
movements = []
midIndex = 0
for i in range(len(inp)):
    if inp[i] == "":
        midIndex = i
        break
    for j in range(len(inp[i])):
        if inp[i][j] == "#":
            wallPositions.add((2 * j, i))
            wallPositions.add((2 * j + 1, i))
        if inp[i][j] == "O":
            b1 = (2 * j, i)
            b2 = (2 * j + 1, i)
            boxPositions.add(b1)
            boxPositions.add(b2)
            boxJoints[b1] = b2
            boxJoints[b2] = b1
        if inp[i][j] == "@":
            playerPos = (2 * j, i)

tr = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}

for i in range(midIndex + 1, len(inp)):
    for m in inp[i]:
        movements.append(tr[m])

def canPushBox(pos, dir, initialCall):
    # print(pos)
    if pos in wallPositions:
        return False
    if pos not in boxPositions:
        return True

    joint = boxJoints[pos]
    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    nextJoint = (joint[0] + dir[0], joint[1] + dir[1])


    ret = False
    if dir == (1, 0):
        ret = canPushBox((pos[0] + 2, pos[1]), dir, False)
    elif dir == (-1, 0):
        ret = canPushBox((pos[0] - 2, pos[1]), dir, False)
    else:
        ret = canPushBox(nextJoint, dir, False) and canPushBox(nextPos, dir, False)

    if initialCall and ret:
        pushBox(pos, dir)

    return ret

def pushBox(pos, dir):
    # print(pos)
    if pos not in boxPositions:
        return

    joint = boxJoints[pos]
    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    nextJoint = (joint[0] + dir[0], joint[1] + dir[1])
    
    if dir == (1, 0):
        pushBox((pos[0] + 2, pos[1]), dir)
    elif dir == (-1, 0):
        pushBox((pos[0] - 2, pos[1]), dir)
    else:
        pushBox(nextPos, dir)
        pushBox(nextJoint, dir)

    boxPositions.remove(pos)
    boxPositions.remove(joint)
    boxPositions.add(nextPos)
    boxPositions.add(nextJoint)

    boxJoints[nextPos] = nextJoint
    boxJoints[nextJoint] = nextPos


def printMaze():
    for c in range(len(inp[0])):
        s = ""
        for r in range(midIndex * 2):
            if (r, c) in wallPositions:
                s += "#"
            elif (r, c) in boxPositions:
                if boxJoints[(r,c)][0] > r:
                    s += "["
                else:
                    s += "]"
            elif (r, c) == playerPos:
                s += "@"
            else:
                s += "."
    #     print(s)
    # print()


# Run through all moves
for move in movements:
    nextPos = (playerPos[0] + move[0], playerPos[1] + move[1])
    if nextPos in wallPositions:
        continue
    if nextPos in boxPositions and not canPushBox(nextPos, move, True):
        continue
    playerPos = nextPos
    # print(move)
    # printMaze()


# Get solution
total = 0
for pos in boxPositions:
    # print(pos)
    if pos[0] < boxJoints[pos][0]:
        total +=  pos[0] + 100 * pos[1]
print(total)

# 12:20 AM