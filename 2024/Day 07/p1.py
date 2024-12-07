inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

problems = []
for s in inp:
    target = int(s[:s.index(":")])
    rest = s[s.index(":") + 2:]
    n = [int(x) for x in rest.split(" ")]
    problems.append([target, n])

def check(target, ns, index, acc):
    if index == len(ns) and acc == target: return True
    if index >= len(ns): return False

    check1 = check(target, ns, index + 1, acc + ns[index]) 
    check2 = check(target, ns, index + 1, acc * ns[index])

    return check1 or check2

sm = 0
for target, ns in problems:
    print("Chekcing ", target)
    if check(target, ns, 0, 0):
        sm += target
print(sm)


# 12:12 AM