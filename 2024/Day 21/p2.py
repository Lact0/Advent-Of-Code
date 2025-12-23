inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

numPad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
dirPad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

numStart = (3, 2)
dirStart = (0, 2)

dTr = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1), (-1, 0): '^', (0, -1): '<', (1, 0): 'v', (0, 1): '>'}

def displacement(start, end):
    return (end[0] - start[0], end[1] - start[1])


numRobots = 2

memo = {}
# Returns the length 
def pressButton(dr, dc, depth):
    # base case: Depth is 0, so dx + dy + 1 (get there and press)
    if depth == 0: return abs(dr) + abs(dc) + 1
    if dr == dc and dc == 0: return 1

    key = (dr, dc, depth)
    if key in memo: return memo[key]

    # First: for dx and dy, we need to get to the 
    # direction and press it once (recurse)
    # plus pressing it dx - 1 or dy - 1 times, as we already
    # did it once
    # Need to find out the distance to correct dir (for dx or dy)
    # So work with numPad

    # 1: Determine what direction buttons I need to press
    b1 = None
    if dr < 0:
        b1 = dirPad['^']
    if dr > 0:
        b1 = dirPad['v']

    b2 = None
    if dc < 0:
        b2 = dirPad['<']
    if dc > 0:
        b2 = dirPad['>']

    toButton = 0
    twoFirst = True
    if b2 is not None:
        twoFirst = dc < 0

        if dc == -2:
            if depth == numRobots:
                twoFirst = dr != -3
            else:
                twoFirst = dr != 1


    db1, db2 = ((),())

    # 2: Determine which order to do them in
    if b1 is not None and b2 is not None:

        # Find distance from start point
        d1 = b1[0] + abs(2 - b1[1])
        d2 = b2[0] + abs(2 - b2[1])

        # Do d2 first
        if twoFirst:
            toButton = pressButton(*displacement(b1, dirStart), depth - 1)
            db1 = displacement(b2, b1)
            db2 = displacement(dirStart, b2)
        else:
            toButton = pressButton(*displacement(b2, dirStart), depth - 1)
            db2 = displacement(b1, b2)
            db1 = displacement(dirStart, b1)

    elif b1 is not None:
        toButton = pressButton(*displacement(b1, dirStart), depth - 1)
        db1 = displacement(dirStart, b1)
    else:
        toButton = pressButton(*displacement(b2, dirStart), depth - 1)
        db2 = displacement(dirStart, b2)


    # 3: Recurse with direction buttons
    b1Len = 1 - abs(dr)
    if b1 is not None:
        b1Len = pressButton(db1[0], db1[1], depth - 1)
    b2Len = 1 - abs(dc)
    if b2 is not None:
        b2Len = pressButton(db2[0], db2[1], depth - 1)

    # Add number of presses to each 
    b1Len += abs(dr) - 1
    b2Len += abs(dc) - 1

    memo[key] = b1Len + b2Len + toButton
    return memo[key]

def findShortestCode(target):
    total = 0

    # Go Through each character and find dx/dy
    pos = numStart
    for c in target:
        targetPos = numPad[c]
        disp = displacement(pos, targetPos)
        length = pressButton(*disp, numRobots)
        total += length

        pos = targetPos
    return total


# Calculate all codes
total = 0
for s in inp:
    l = findShortestCode(s)
    n = int(s[:-1])
    print(s, l)
    total += n * l
print(total)

