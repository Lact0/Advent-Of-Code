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
for i in range(1, 10000000): #totalSeconds):
    newPositions = []
    for p, v in robots:
        newP = p + v * (i)
        newP = (int(newP.real) % roomWidth) + (int(newP.imag) % roomHeight) * 1j
        newPositions.append((newP.real, newP.imag))

    tree = True
    for x in range(len(newPositions)):
        if newPositions[x] in newPositions[x+1:]:
            tree = False
            break
    if tree:
        print("WE HAVE FOUND IT IN ITERATION", i)
    
        print(i)
        for x in range(roomWidth):
            arr = ""
            for y in range(roomHeight):
                if (x, y) in newPositions:
                    arr += "0"
                else:
                    arr += '.'
            print(arr)
        print()
        input()
    


# Terrible quesiton.
# I looked at the subreddit to see that they were asking for when
# no bot was overlapping. Why the heck would that be the case?
# There are a bunch of bots not on the tree. There's no reason
# that they couldn't be on top of each other while the tree
# was there.

#SUS: 39, 99, 140, 202, 241