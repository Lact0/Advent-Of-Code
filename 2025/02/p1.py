
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

ranges = inp[0].split(',')
ranges = [[int(x) for x in y.split("-")] for y in ranges]


def isInvalid(n):
    l = len(str(n))
    return (l % 2 == 0) and str(n)[:l // 2] == str(n)[l // 2:]

s = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        if isInvalid(i):
            s += i
print(s)