inp = []
with open("Day 8/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

path = inp[0]

map = {}
for fork in inp[2:]:
    map[fork.split()[0]] = {"L": fork.split()[2][1:4], "R": fork.split()[3][0:3]}

ghostNodes = [x for x in map.keys() if x[2] == "A"]
loops = []
for ghost in ghostNodes:
    #{node: [ind]}
    zs = []
    i = 0
    while not (ghost[-1] == "Z" and i % len(path) in [x % len(path) for x in zs]):
        if ghost[-1] == "Z":
            zs.append(i)
        ghost = map[ghost][path[i % len(path)]]
        i += 1
    print(zs, [ghost, i])
    loops.append([zs[0], i - zs[0]])


t = max([x[0] for x in loops])
loops = [[(t - f) % l, l] for f, l in loops]

def getLCM(l):
    m = 293
    for n in l:
        m *= n / 293
    return m

while sum([x[0] for x in loops]) > 0:
    lcm = getLCM([x[1] for x in loops if x[0] == 0])
    loops = [[(x[0] + lcm) % x[1], x[1]] for x in loops]
    t += lcm

print(t)

