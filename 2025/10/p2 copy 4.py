
# This one will be the rref
# First answer is 48707

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
    targets = tuple([int(x) for x in row[-1][1:-1].split(',')])
    machines.append((targets, buttons))


def solve(targets, buttons, memo = {}):
    if targets in memo:
        return memo[targets]
    
    if all([x == 0 for x in targets]):
        return 0

    min_presses = 1000000000000000000000000000
    for button in buttons:
        new_targets = tuple([targets[i] - (i in button) for i in range(len(targets))])
        if any([x < 0 for x in new_targets]):
            continue

        presses = 1 + solve(new_targets, buttons, memo)
        min_presses = min(presses, min_presses)

    memo[targets] = min_presses
    return min_presses


s = 0
for targets, buttons in machines:
    m = solve(targets, buttons)
    print(m)
    s += m

print(s)