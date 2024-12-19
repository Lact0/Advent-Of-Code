inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

towels = [i.strip(",") for i in inp[0].split()]
targets = [inp[i] for i in range(2, len(inp))]

memo = {}
def canBeMade(target):
    if target == "": return True
    if target in memo: return memo[target]

    can = False
    for towel in towels:
        if len(towel) > len(target): continue
        if target[:len(towel)] != towel: continue
        if canBeMade(target[len(towel):]):
            can = True
            break
    memo[target] = can
    return can


total = 0
i = 0
for target in targets:
    if canBeMade(target): total += 1
    i += 1
print(total)

# 12:07 AM