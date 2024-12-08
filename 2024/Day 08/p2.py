inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

# Find all antennas
antennas = {}
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == '.': continue
        if inp[i][j] not in antennas.keys():
            antennas[inp[i][j]] = []
        antennas[inp[i][j]].append([i, j])

def isValid(i, j):
    return i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0])

antinodes = set()
for freq in antennas.keys():

    for i, j in antennas[freq]:
        for x, y in antennas[freq]:
            if i == x and y == j: continue
            vec = [x - i, y - j]

            n = 0
            while True:
                antinode = [x + n * vec[0], y + n * vec[1]]

                if isValid(antinode[0], antinode[1]):
                    antinodes.add(str(antinode[0]) + "," + str(antinode[1]))
                else:
                    break
                n += 1

print(len(antinodes))

# 12:20 AM