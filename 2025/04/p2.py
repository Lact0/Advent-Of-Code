
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [list(r) for r in inp]

def is_valid(r, c):
    return r >= 0 and c >= 0 and r < len(inp) and c < len(inp[r])

def is_free(r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if is_valid(nr, nc) and inp[nr][nc] == '@':
                count += 1
    return count < 4

s = 0
removed = True
while removed == True:
    removed = False
    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if inp[r][c] == '@' and is_free(r, c):
                # print(r, c)
                s += 1
                inp[r][c] = '.'
                removed = True
print(s)
            