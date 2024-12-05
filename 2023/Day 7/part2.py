inp = []
with open("Day 7/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

hands = [[x.split()[0], int(x.split()[1])] for x in inp]

ranks = "J23456789TQKA"

def getVal(hand):
    val = 0
    for i in range(len(hand)):
        val += ranks.index(hand[i]) * (100 ** (4 - i))
    occ = {}
    for i in hand:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    
    if "J" in occ.keys() and len(occ) != 1:
        jokers = occ.pop("J")
        occ[max(occ, key=occ.get)] += jokers

    if len(occ) == 1:
        val += 6 * (100 ** 5)
    elif len(occ) == 2 and (4 in occ.values()):
        val += 5 * (100 ** 5)
    elif len(occ) == 2:
        val += 4 * (100 ** 5)
    elif 3 in occ.values():
        val += 3 * (100 ** 5)
    elif len(occ) == 3 and (2 in occ.values()):
        val += 2 * (100 ** 5)
    elif len(occ) == 4:
        val += 1 * (100 ** 5)
    
    return val


hands.sort(key=lambda hand: getVal(hand[0]))
winnings = [hands[i][1] * (i + 1) for i in range(len(hands))]
print(sum(winnings))