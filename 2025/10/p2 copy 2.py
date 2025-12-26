
# This one will first sort the buttons and return the first sol
# ASSUMPTION DOES NOT WORK

inp = []
with open("a.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [x.split() for x in inp]

machines = []
for row in inp:
    buttons = []
    for i in range(1, len(row) - 1):
        buttons.append([int(x) for x in row[i][1:-1].split(',')])
    target = [int(x) for x in row[-1][1:-1].split(',')]
    buttons.sort(reverse=True, key=lambda x: len(x))
    machines.append((target, buttons))

# print(machines)

def gen_vars_eqs(target, buttons):
    vars = [-1 for _ in buttons]
    eqs = []
    for i in range(len(target)):
        rhs = target[i]
        lhs = [j for j in range(len(buttons)) if i in buttons[j]]
        eqs.append((rhs, lhs))
    return vars, eqs

def solve(target, buttons):
    sol, valid = solve_helper(*gen_vars_eqs(target, buttons))
    return sol, valid

# returns (new_vars, new_eqs, valid)

def deduce_vars(vars, eqs):

    while 1 in [len(x[1]) for x in eqs]:
        eq_ind = [len(x[1]) for x in eqs].index(1)
        rhs, lhs = eqs[eq_ind]
        var = lhs[0]

        vars, eqs, valid = fix_var(vars, eqs, var, rhs)
        if not valid:
            return vars, eqs, False
    
    new_eqs = []
    for eq in eqs:
        if eq[0] != 0:
            new_eqs.append(eq)

    return vars, new_eqs, True

def upper_var_val(eqs, var):
    m = 10000000000000000000000000000000000000
    for rhs, lhs in eqs:
        if var in lhs and rhs < m:
            m = rhs
    return m

def copy_eqs(eqs):
    new_eqs = []
    for rhs, lhs in eqs:
        new_eqs.append((rhs, lhs.copy()))
    return new_eqs

# returns (new_vars, new_eqs, valid)
def fix_var(vars, eqs, var, n):
    # print("FIXING VAR", var, "=", n, "IN", vars, eqs)
    new_eqs = copy_eqs(eqs)
    new_vars = vars.copy()
    new_vars[var] = n

    # reduce equations with new value
    for i in range(len(new_eqs)):
        rhs, lhs = new_eqs[i]
        if var in lhs:

            if rhs - n < 0: # value too large
                return new_vars, new_eqs, False
            if len(lhs) == 1 and rhs != n: # 0 = n contradiciton
                return new_vars, new_eqs, False

            lhs.remove(var)
            new_eqs[i] = (rhs - n, lhs)
    return new_vars, new_eqs, True



# vars: List[int], size of buttons, each has -1 if not fixed
# eqs: tuple[int, list(int)] first stores the rhs (int), then all variables that add to that
# returns list of valid variable assignments
# It will only fix ONE variable at a time.
def solve_helper(vars: list[int], eqs: list[tuple[int, list[int]]]):

    # print("BEFORE DEDUCTION:", vars, eqs)

    # find fixed vars
    vars, eqs, valid = deduce_vars(vars, eqs)
    if not valid:
        return [], False

    # print("AFTER DEDUCTION:", vars, eqs)

    # if all variables are fixed, return sol
    if -1 not in vars and all([x[0] == 0 for x in eqs]):
        # print("     RETURNING, FOUND SOL", vars)
        return vars, True

    free_var = vars.index(-1)
    upper_bound = upper_var_val(eqs, free_var)
    for i in range(upper_bound + 1):
        # print("FIXING", free_var, "TO", i)
        new_vars, new_eqs, valid = fix_var(vars, eqs, free_var, i)
        # print("     before fixing:", new_vars, new_eqs)
        # print("     after fixing:", new_vars, new_eqs, valid)
        # input()
        if not valid: # if it's not valid, it's too large, so any larger is worse
            break

        # recurse with new assignment
        sol, valid = solve_helper(new_vars, new_eqs)
        if valid:
            return sol, valid
    
    return [], False


s = 0
i = 0
for machine in machines:
    print(i)
    i += 1
    target, buttons = machine
    vars, eqs = gen_vars_eqs(target, buttons)
    # print("BEFORE:", vars, eqs)
    # print("AFTER:", deduce_vars(vars, eqs))
    # print(solve(target, buttons))
    sol, valid = solve(target, buttons)
    print(sol, sum(sol))
#     m = 1000000
#     for sol in sols:
#         if sum(sol) < m:
#             m = sum(sol)
#     # print(m)
#     s += m
# print(s)



