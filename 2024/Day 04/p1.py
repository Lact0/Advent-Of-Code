inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def isValidPos(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

target = "XMAS"
DIR = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

count = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):

        # Check every direction
        for dir in DIR:
            found = True
            for k in range(len(target)):
                newI = i + dir[0] * k
                newJ = j + dir[1] * k
                if not (isValidPos(newI, newJ) and inp[newI][newJ] == target[k]):
                    found = False
                    break
            if found: count += 1

print(count)

# 12:07 AM