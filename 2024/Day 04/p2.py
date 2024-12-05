inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def isValidPos(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

target = "XMAS"
DIR = [[1, 1], [1, -1]]

count = 0
for i in range(1, len(inp) - 1):
    for j in range(1, len(inp[0]) - 1):
        if inp[i][j] != "A": continue

        found = True
        for dir in DIR:
            s = inp[i + dir[0]][j + dir[1]] + inp[i - dir[0]][j - dir[1]]
            if not (s == "SM" or s == "MS"):
                found = False
                break
        if found: count += 1


print(count)

# 12:12 AM