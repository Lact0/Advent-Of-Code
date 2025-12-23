
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

ranges = inp[0].split(',')
ranges = [[int(x) for x in y.split("-")] for y in ranges]

def isPeriod(n, w):
    l = len(str(n))
    if l % w != 0:
        return False

    first = str(n)[:w]
    for i in range(l // w):
        if first != str(n)[w*i:w*(i+1)]:
            return False
    return True

def isInvalid(n):
    for i in range(1, len(str(n))):
        if isPeriod(n, i):
            return True
    return False

s = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        if isInvalid(i):
            s += i
print(s)