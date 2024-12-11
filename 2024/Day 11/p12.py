inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

#Number, numBlinksLeft
nBlinks = 75
inp = [[int(x), nBlinks] for x in inp[0].split(" ")]

memo = {}

def numRocks(n, ticks):
    key = (n,ticks)
    if key in memo.keys():
        return memo[(n,ticks)]

    if ticks == 0:
        return 1

    if n == 0:
        ret = numRocks(1, ticks - 1)
        memo[key] = ret
        return ret
    
    if len(str(n)) % 2 == 0:
        mid = len(str(n)) // 2
        ret = numRocks(int(str(n)[:mid]), ticks - 1) + numRocks(int(str(n)[mid:]), ticks - 1)
        memo[key] = ret
        return ret
    
    ret = numRocks(n * 2024, ticks - 1)
    memo[key] = ret
    return ret

sm = 0
for n, ticks in inp:
    sm += numRocks(n, ticks)
print(sm)

# 12:13
