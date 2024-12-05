inp = []
with open("Day 6/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

time, bestDist = [int("".join(inp[0].split()[1:])), int("".join(inp[1].split()[1:]))]

rt = (time * time - 4 * bestDist) ** .5
q1 = (time + rt) / 2
q2 = (time - rt) / 2
print(int(q1 - q2))