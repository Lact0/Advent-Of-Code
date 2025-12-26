
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [x.split() for x in inp]

machines = []
for row in inp:
    buttons = []
    for i in range(1, len(row) - 1):
        buttons.append([int(x) for x in row[i][1:-1].split(',')])
    target = [int(x) for x in row[-1][1:-1].split(',')]
    machines.append((target, buttons))

def calc(buttons, coeff):
    ret = [0 for i in target]
    for i in range(len(buttons)):
        for b in buttons[i]:
            ret[b] += coeff[i]
    return ret

def is_valid(target, buttons, coeff):
    vect = calc(buttons, coeff)
    for i in range(len(vect)):
        if vect[i] > target[i]:
            return False
    return True

def solve(buttons, target):
    # print(buttons, target)
    if all([x == 0 for x in target]):
        return [[0 for _ in buttons]]
    if len(buttons) == 0:
        return []
    
    sols = []
    for n in range(max(target) + 1):
        print("  " * (6 - len(buttons)), n, buttons, target)
        # get new target
        new_target = [x for x in target]
        valid = True
        for i in buttons[0]:
            new_target[i] -= n
            if new_target[i] < 0:
                valid = False
                break
        if not valid:
            break

        sub_sols = solve(buttons[1:], new_target)
        for sub_sol in sub_sols:
            sols.append([n] + sub_sol)

    return sols

s = 0
for target, buttons in machines:
    m = 1000000000000000000000
    for sol in solve(buttons, target):
        if sum(sol) < m:
            m = sum(sol)
    print(m)
    s += m
print(s)