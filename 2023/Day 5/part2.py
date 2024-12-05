from collections import deque 

inp = []
with open("Day 5/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

def overlap(n1, l1, n2, l2):
    return max(n1, n2) < min(n1 + l1, n2 + l2)

seeds = [int(x) for x in inp[0].split()[1:]]
seeds = deque([[seeds[2 * x], seeds[2 * x + 1]] for x in range(int(len(seeds) / 2))])

steps = []
for row in inp[1:]:
    if row == '': continue
    if row[-1] == ":":
        steps.append([])
        continue
    steps[-1].append([int(x) for x in row.split()])

for maps in steps:
    newSeeds = deque()
    while seeds:
        n, l = seeds.popleft()
        split = False
        for map in maps:
            if not overlap(n, l, map[1], map[2]):
                continue
            #Check the 4 ways it could be overlapped
            if n < map[1] and map[2] + map[1] < l + n: #Interval contains map
                newSeeds.append([map[0], map[2]])
                seeds.append([n, map[1] - n])
                seeds.append([map[1] + map[2], n + l - map[1] - map[2]])
            elif n > map[1] and l + n <= map[2] + map[1]: #Map contians interval
                newSeeds.append([n + map[0] - map[1], l])
            elif n > map[1]: #Overlap on the left of the interval
                newSeeds.append([map[0] + n - map[1], map[2] + map[1] - n])
                seeds.append([map[1] + map[2], n + l - map[1] - map[2]])
            elif n < map[1]: #Overlap on the right of the interval
                newSeeds.append([map[0], l + n - map[1]])
                seeds.append([n, map[1] - n])
                
            else: #Interval is the same as the map
                newSeeds.append([map[0], l])
            split = True
            break

        if not split:
            newSeeds.append([n, l])
    seeds = newSeeds

print(min([x[0] for x in seeds]))