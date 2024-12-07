inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append([i for i in row.strip("\n")])

startPos = []

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == '^':
            startPos = [i, j]
            break

def turn(vel):
    return [vel[1], -vel[0]]

def outside(pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(inp) or pos[1] >= len(inp[0])


def checkLoop(ob):
    inp[ob[0]][ob[1]] = '#'

    pos = startPos.copy()
    vel = [-1, 0]
    loops = False
    seenStates = set((tuple(pos), tuple(vel)))
    while not outside(pos):
        state = (tuple(pos), tuple(vel))
        if state in seenStates:
            loops = True
            break
        seenStates.add(state)

        front = [pos[0] + vel[0], pos[1] + vel[1]]
        if not outside(front) and inp[front[0]][front[1]] == '#':
            vel = turn(vel)
        else:
            pos[0] += vel[0]
            pos[1] += vel[1]

    inp[ob[0]][ob[1]] = '.'
    return loops



sm = 0
for i in range(len(inp)):
    print(i)
    for j in range(len(inp[0])):
        if inp[i][j] == '#': continue
        if [i,j] == startPos: continue

        if checkLoop([i, j]): sm += 1
print(sm)
        
# Went to 1:30 AM, worked from 11:00 AM to 12:24 AM
# IT WAS BECAUSE OF THE else: THAT NEEDS TO BE DONE AFTER TURNING