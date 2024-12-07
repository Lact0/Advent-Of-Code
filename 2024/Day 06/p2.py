inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

pos = []
obstacles = set()

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j] == '^':
            pos = [i, j]
        if inp[i][j] == '#':
            obstacles.add(str(i) + "," + str(j))

initPos = pos.copy()
vel = [-1, 0]

def turn(vel):
    return [vel[1], -vel[0]]
def isValid(p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < len(inp) and p[1] < len(inp[0])

posSet = set()
while isValid(pos):
    posSet.add(",".join(str(x) for x in pos))
    newPos = [pos[0] + vel[0], pos[1] + vel[1]]
    if str(newPos[0]) + "," + str(newPos[1]) in obstacles:
        vel = turn(vel)
    pos[0] += vel[0]
    pos[1] += vel[1]
posSet.remove(str(initPos[0]) + "," + str(initPos[1]))
posSet = [[int(x) for x in i.split(",")] for i in posSet]

sm = 0
n = 0
for i, j in posSet:
        print(n)
        n += 1
        obstacleKey = str(i) + "," + str(j)
        if obstacleKey in obstacles: continue
        if [i, j] == initPos: continue
        obstacles.add(obstacleKey)

        # Try to find loop
        seenSet = set()
        pos = initPos.copy()
        vel = [-1, 0]
        while True:
            state = str(pos[0]) + "," + str(pos[1]) + "," + str(vel[0]) + "," + str(vel[1])
            if state in seenSet:
                sm += 1
                break
            seenSet.add(state)

            newPos = [pos[0] + vel[0], pos[1] + vel[1]]
            if not isValid(newPos): break
            if str(newPos[0]) + "," + str(newPos[1]) in obstacles:
                vel = turn(vel)
            pos = [pos[0] + vel[0], pos[1] + vel[1]]


        obstacles.remove(obstacleKey)

print(sm)


exit()
# posSet = set()
sm = 0
while isValid(pos):
    # posSet.add(",".join(str(x) for x in pos))
    newPos = [pos[0] + vel[0], pos[1] + vel[1]]
    if newPos in obstacles:
        vel = turn(vel)

    # Try adding obstacle in front
    tempPos = pos.copy()
    tempVel = vel.copy()
    obstacles.append(newPos)
    seenStateSet = set()
    while True:
        state = ",".join(str(i) for i in tempPos + tempVel)
        if state in seenStateSet:
            sm += 1
            break
        seenStateSet.add(state)
        if not isValid(tempPos): break
        tempNewPos = [tempPos[0] + tempVel[0], tempPos[1] + tempVel[1]]
        if tempNewPos in obstacles:
            tempVel = turn(tempVel)
        tempPos[0] += tempVel[0]
        tempPos[1] += tempVel[1]

    obstacles.remove(newPos)

    # Step forward
    pos[0] += vel[0]
    pos[1] += vel[1]


print(sm)
exit()

hitPositions = [[int(x) for x in i.split(",")] for i in posSet]
hitPositions.remove(initPos)

def checkLoop(obstaclePos):
    obstacles.append(obstaclePos)
    vel = [-1, 0]
    pos = initPos.copy()
    while True:
        newPos = [pos[0] + vel[0], pos[1] + vel[1]]
        if newPos == obstaclePos: break
        if not isValid(newPos): return False
        if newPos in obstacles:
            vel = turn(vel)
        pos[0] += vel[0]
        pos[1] += vel[1]

    # Found obstacle, pos is right before it and vel is pointing towards it

    # Start loop attempt
    vel = turn(vel)
    while True:
        newPos = [pos[0] + vel[0], pos[1] + vel[1]]
        if newPos == obstaclePos: return True
        if newPos in obstacles: vel = turn(vel)
        if not isValid(newPos): return False
        pos[0] += vel[0]
        pos[1] += vel[1]
    

sm = 0
for ob in hitPositions:
    if checkLoop(ob): sm += 1
    obstacles.remove(ob)

print(sm)



    


# 12:08