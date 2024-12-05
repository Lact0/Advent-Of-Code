inp = []
with open("Day 3/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def validPos(r, c):
    return r >= 0 and r < len(inp) and c >= 0 and c < len(inp[r])

def isSymbol(r, c):
    return (not inp[r][c].isdigit()) and (inp[r][c] != ".")

def hasSymbol(r, c, l):
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + l + 1):
            if validPos(i, j) and isSymbol(i, j):
                return True
    return False

sum = 0
for i in range(len(inp)):
    j = 0
    curNumber = ''
    while j < len(inp[i]):
        if inp[i][j].isdigit():
            curNumber += inp[i][j]
        elif len(curNumber) != 0:
            if hasSymbol(i, j - len(curNumber), len(curNumber)):
                sum += int(curNumber)
            curNumber = ''
        j += 1
print(sum)
