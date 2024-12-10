inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [[int(x) for x in i] for i in inp]

starts = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 0:
            starts.append([i, j])

def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def findTrails(start):

    trailEndSet = set()
    queue = [[start[0], start[1], 0, ""]]
    while len(queue) > 0:
        x, y, n, trail = queue[0]
        queue = queue[1:]

        trail += "," + str(x) + "," + str(y)

        if n == 9:
            trailEndSet.add(trail)
            continue

        for dx, dy in DIR:
            newX = x + dx
            newY = y + dy
            if isValid(newX, newY) and inp[newX][newY] == n + 1:
                queue.append([newX, newY, n + 1, trail])
    return len(trailEndSet)
                



totalSum = 0
for start in starts:
    totalSum += findTrails(start)
print(totalSum)

# 12:13 AM