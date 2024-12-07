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
    if index >= len(ns) or acc > target: return False

    check1 = check(target, ns, index + 1, acc + ns[index]) 

    check2 = False
    if acc == 0:
        check2 = check(target, ns, index + 1, ns[index])
    else: check2 = check(target, ns, index + 1, acc * ns[index])

    check3 = check(target, ns, index + 1, int(str(acc) + str(ns[index])))

    return (check1 or check2) or check3

sm = 0
n = 0
for target, ns in problems:
    print(n)
    n += 1
    if check(target, ns, 0, 0):
        sm += target
print(sm)

# 12:29 AM