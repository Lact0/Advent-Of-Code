inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

# robot is (pos, vel)
robots = []

for row in inp:
    ps, vs = row.split(" ")

    px = int(ps[2:ps.index(",")])
    py = int(ps[ps.index(",")+1:])

    vx = int(vs[2:vs.index(",")])
    vy = int(vs[vs.index(",")+1:])

    robots.append((px + py * 1j, vx + vy * 1j))

roomWidth = 101
roomHeight = 103
totalSeconds = 100

def checkQuadrant(p):
    if p.real < roomWidth // 2:
        if p.imag < roomHeight // 2:
            return 0
        elif p.imag > roomHeight // 2:
            return 1
    if p.real > roomWidth // 2:
        if p.imag < roomHeight // 2:
            return 2
        elif p.imag > roomHeight // 2:
            return 3
    return -1


quads = [0, 0, 0, 0]
for p, v in robots:
    newP = p + v * totalSeconds
    newP = (int(newP.real) % roomWidth) + (int(newP.imag) % roomHeight) * 1j
    ind = checkQuadrant(newP)
    if ind >= 0:
        quads[ind] += 1

print(quads)
print(quads[0] * quads[1] * quads[2] * quads[3])
