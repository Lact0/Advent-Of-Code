
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [r.split() for r in inp]
inp[:-1] = [[int(x) for x in r] for r in inp[:-1]]


total = 0
for c in range(len(inp[0])):
    calc = inp[0][c]
    for r in range(1, len(inp) - 1):
        if inp[-1][c] == '+':
            calc += inp[r][c]
        else:
            calc *= inp[r][c]
    total += calc

print(total)