inp = []
with open("Day 3/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def validPos(r, c):
    return r >= 0 and r < len(inp) and c >= 0 and c < len(inp[r])

def isSymbol(r, c):
    return (not inp[r][c].isdigit()) and (inp[r][c] != ".")

def findFullNumber(r, c):
    ind = c + 1
    n = inp[r][c]
    while validPos(r, ind) and inp[r][ind].isdigit():
        n += inp[r][ind]
        ind += 1
    ind = c - 1
    while validPos(r, ind) and inp[r][ind].isdigit():
        n = inp[r][ind] + n
        ind -= 1
    return [[r, ind + 1], int(n)]

sum = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] != "*":
            continue
        nums = []
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if validPos(k, l) and inp[k][l].isdigit():
                    nums.append(findFullNumber(k, l))
        names = []
        ns = []
        for name, n in nums:
            if name not in names:
                names.append(name)
                ns.append(n)
        if len(ns) == 2:
            sum += ns[0] * ns[1]

print(sum)
