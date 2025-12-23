
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

op_ind = 0
total = 0
cur = 0
for c in range(len(inp[0])):
    if all([row[c] == " " for row in inp]):
        total += cur
        op_ind = c + 1
        cur = 0
        continue
    
    n = 0
    for r in range(len(inp) - 1):
        if inp[r][c] == ' ':
            continue
        n = n * 10 + int(inp[r][c])

    if cur == 0:
        cur = n
    else:
        if inp[-1][op_ind] == '+':
            cur += n
        else:
            cur *= n
total += cur
print(total)