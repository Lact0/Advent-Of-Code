inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))


def getTokens(a, b, t):

    delta = a[0] * b[1] - b[0] * a[1]
    if delta == 0: return 0
    numA = (t[0] * b[1] - b[0] * t[1]) / delta
    numB = (a[0] * t[1] - t[0] * a[1]) / delta

    if int(numA) != numA or int(numB) != numB:
        return 0
    return int(numA * 3 + numB)



total = 0
for i in range(0, len(inp), 4):
    l1 = inp[i].split(' ')
    l2 = inp[i+1].split(' ')
    l3 = inp[i+2].split(' ')

    a = (int(l1[2][2:-1]), int(l1[3][2:]))
    b = (int(l2[2][2:-1]), int(l2[3][2:]))
    e = (int(l3[1][2:-1]), int(l3[2][2:]))
    e = (e[0] + 10_000_000_000_000, e[1] + 10_000_000_000_000)
    total += getTokens(a, b, e)
print(total)
