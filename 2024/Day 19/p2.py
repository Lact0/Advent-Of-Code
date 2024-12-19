# import sys
# sys.setrecursionlimit(10000000)


inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

towels = [i.strip(",") for i in inp[0].split()]
targets = [inp[i] for i in range(2, len(inp))]

memo = {}
def waysToBeMade(target):
    if target == "": return 1
    if target in memo: return memo[target]


    total = 0
    for towel in towels:
        if len(towel) > len(target): continue
        if target[:len(towel)] != towel: continue
        total += waysToBeMade(target[len(towel):])

    memo[target] = total
    return total


total = 0
i = 0
for target in targets:
    total += waysToBeMade(target)
    i += 1
print(total)

# 12:11 AM