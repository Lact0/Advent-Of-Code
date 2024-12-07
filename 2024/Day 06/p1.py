inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

pos = []
obstacles = []

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j] == '^':
            pos = [i, j]
        if inp[i][j] == '#':
            obstacles.append([i,j])

vel = [-1, 0]

def turn(vel):
    return [vel[1], -vel[0]]
def isValid(p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < len(inp) and p[1] < len(inp[0])

posSet = set()
while isValid(pos):
    posSet.add(",".join(str(x) for x in pos))
    newPos = [pos[0] + vel[0], pos[1] + vel[1]]
    if newPos in obstacles:
        vel = turn(vel)
    pos[0] += vel[0]
    pos[1] += vel[1]

print(len(posSet))

# 12:08