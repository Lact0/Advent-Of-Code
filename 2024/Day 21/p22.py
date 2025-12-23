inp = []
with open("s.txt", "r") as file:
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


def displacement(start, end):
    return (end[0] - start[0], end[1] - start[1])

memo = {}
# Returns the length 
def pressButton(sr, sc, fr, fc, depth):

    key = (sr, sc, fr, fc, depth)
    if key in memo: return memo[key]

    dr = fr - sr
    dc = fc - sc

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
            toButton = pressButton(*b1, *dirStart, depth - 1)
            db1 = (*b2, *b1)
            db2 = (*dirStart, *b2)
        else:
            toButton = pressButton(*b2, *dirStart, depth - 1)
            db2 = (*b1, *b2)
            db1 = (*dirStart, *b1)

    elif b1 is not None:
        toButton = pressButton(*b1, *dirStart, depth - 1)
        db1 = (*dirStart, *b1)
    else:
        toButton = pressButton(*b2, *dirStart, depth - 1)
        db2 = (*dirStart, *b2)


    # 3: Recurse with direction buttons
    b1Len = 1 - abs(dr)
    if b1 is not None:
        b1Len = pressButton(*db1, depth - 1)
    b2Len = 1 - abs(dc)
    if b2 is not None:
        b2Len = pressButton(*db2, depth - 1)


    # Add number of presses to each 
    b1Len += abs(dr) - 1
    b2Len += abs(dc) - 1

    mn = b1Len + b2Len + toButton


    # if depth == 0: return abs(dr - sr) + abs(dc - sc) + 1

    # # Try all paths
    # mn = 99999999999999999999999999

    # # If they are horizontal
    # if sr == dr:
    #     button = ()
    #     if sc < dc:
    #         button = dirPad['>']
    #     else:
    #         button = dirPad['<']
        
    #     # Go to button, press, go back
    #     numPresses = abs(dc - sc) - 1
        
    #     there = pressButton(*dirStart, *button, depth - 1)
    #     back = pressButton(*button, *dirStart, depth - 1)

    #     mn = there + back + numPresses

    # # IF they are vertical
    # elif sc == dc:
    #     button = ()
    #     if sr < dr:
    #         button = dirPad['v']
    #     else:
    #         button = dirPad['^']
        
    #     # Go to button, press, go back
    #     numPresses = abs(dr - sr) - 1
        
    #     there = pressButton(*dirStart, *button, depth - 1)
    #     back = pressButton(*button, *dirStart, depth - 1)

    #     mn = there + back + numPresses

    # # Otherwise, check both lanes
    # else:
    #     corner1 = (sr, dc)
    #     corner2 = (dr, sc)

    #     # Remove corners if invalid
    #     if depth == numRobots:
    #         if sr == 3 and dc == 0: corner1 = None
    #         if dr == 3 and sc == 0: corner2 = None
    #     else:
    #         if sr == 0 and dc == 0: corner1 = None
    #         if dr == 0 and sc == 0: corner2 = None


    #     # Get buttons
    #     button1 = ()
    #     if sc < dc:
    #         button1 = dirPad['>']
    #     else:
    #         button1 = dirPad['<']

    #     button2 = ()
    #     if sr < dr:
    #         button2 = dirPad['v']
    #     else:
    #         button2 = dirPad['^']
        
    #     # Calculate paths
    #     presses = abs(dc - sc) - 1 + abs(dr - sc) - 1
        
    #     there1 = pressButton(*dirStart, *button1, depth - 1)
    #     there2 = pressButton(*dirStart, *button2, depth - 1)
    #     mid1 = pressButton(*button1, *button2, depth - 1)
    #     mid2 = pressButton(*button2, *button1, depth - 1)
    #     back1 = pressButton(*button2, *dirStart, depth - 1)
    #     back2 = pressButton(*button1, *dirStart, depth - 1)

    #     path1 = there1 + mid1 + back1 + presses
    #     path2 = there2 + mid2 + back2 + presses

    #     mn = min(path1, path2)


    memo[key] = mn
    return mn

def findShortestCode(target):
    total = 0

    # Go Through each character and find dx/dy
    pos = numStart
    for c in target:
        targetPos = numPad[c]
        length = pressButton(*pos, *targetPos, numRobots)
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


