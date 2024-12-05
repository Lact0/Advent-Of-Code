inp = []
with open("Day 5/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def updateSeed(seed, map):
    for rule in map:
        if seed >= rule[1] and seed <= rule[1] + rule[2] - 1:
            return seed - rule[1] + rule[0] 
    return seed

seeds = [int(x) for x in inp[0].split()[1:]]

maps = []
for row in inp[1:]:
    if row == '': continue
    if row[-1] == ":":
        maps.append([])
        continue
    maps[-1].append([int(x) for x in row.split()])

for map in maps:
    seeds = [updateSeed(x, map) for x in seeds]

print(min(seeds))