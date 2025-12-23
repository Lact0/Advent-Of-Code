inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

numPad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
dirPad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

numStart = (3, 2)
dirStart = (0, 2)

dTr = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1), (-1, 0): '^', (0, -1): '<', (1, 0): 'v', (0, 1): '>'}

# Returns all possible direciton strings to move to target
def pressButton(pos, target, pad):
    ret = set()
    targetPos = pad[target]
    if pos == targetPos: return "A"

    # Account for ways to get there from they y-direction
    if targetPos[1] > pos[1] and (pos[0], pos[1] + 1) in pad.values():
        ySet = pressButton((pos[0], pos[1] + 1), target, pad)
        [ret.add('>' + i) for i in ySet]
    elif targetPos[1] < pos[1] and (pos[0], pos[1] - 1) in pad.values():
        ySet = pressButton((pos[0], pos[1] - 1), target, pad)
        [ret.add('<' + i) for i in ySet]
    
    # Find all values with a change in x position
    if targetPos[0] > pos[0] and (pos[0] + 1, pos[1]) in pad.values():
        xSet = pressButton((pos[0] + 1, pos[1]), target, pad)
        [ret.add('v' + i) for i in xSet]
    elif targetPos[0] < pos[0] and (pos[0] - 1, pos[1]) in pad.values():
        xSet = pressButton((pos[0] - 1, pos[1]), target, pad)
        [ret.add('^' + i) for i in xSet]

    return ret

def pressSequence(pos, target, pad):
    moveSet = set()
    for i in target:
        allWays = pressButton(pos, i, pad)
        pos = pad[i]
        newSet = set()
        for j in moveSet:
            for k in allWays:
                newSet.add(j + k)
        if len(moveSet) == 0: moveSet = allWays
        else: moveSet = newSet

    return moveSet


# Returns a sequence of all ways to make all targets
def controlRobot(targetSet):
    totalSet = set()
    for target in targetSet:
        # Set of all ways to get this target
        s = pressSequence(dirStart, target, dirPad)
        totalSet.update(s)
    return totalSet



def findShortestCode(target):
    # Step 1: Find all shortest for the final numpad
    set1 = pressSequence(numStart, target, numPad)

    # Do twice: control robots
    control1 = controlRobot(set1)
    final = controlRobot(control1)

    # Find minimal code
    minLength = 99999999999999999999999999
    minCode = ()
    for code in final:
        if len(code) < minLength:
            minLength = len(code)
            minCode = code
    
    return minLength, minCode
    

# Calculate all codes
total = 0
for s in inp:
    l, code = findShortestCode(s)
    print(s, code, l)
    n = int(s[:-1])
    total += n * l
print(total)

# 11:55 PM CT (12:55 AM ET)