
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [tuple(int(x) for x in y.split(',')) for y in inp]

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

max_area = 0
for i in range(len(inp)):
    for j in range(i + 1, len(inp)):
        max_area = max(area(inp[i], inp[j]), max_area)
print(max_area)
