
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))
           
ranges = []
mid_row = 1
for row in inp:
    if row == "":
        break
    mid_row += 1
    ranges.append([int(x) for x in row.split("-")])

ids = []
for i in range(mid_row, len(inp)):
    ids.append(int(inp[i]))
    
def in_range(r, i):
    return i >= r[0] and i <= r[1]

s = 0
for id in ids:
    for r in ranges:
        if in_range(r, id):
            s += 1
            break

print(s)