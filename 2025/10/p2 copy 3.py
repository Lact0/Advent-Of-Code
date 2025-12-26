
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
    targets = [int(x) for x in row[-1][1:-1].split(',')]
    # buttons.sort(reverse=True, key=lambda x: len(x)) rearranges columns of matrices
    machines.append((targets, buttons))


matrices = []
for targets, buttons in machines:
    matrix = [[(row in button) * 1 for button in buttons] + [targets[row]] for row in range(len(targets))]
    matrices.append(matrix)



# Functions for reducing matrix
def div_row(mat, row, n):
    mat[row] = [x / n for x in mat[row]]

def sub_row(mat, fro, to, n):
    for i in range(len(mat[0])):
        mat[to][i] -= mat[fro][i] * n

def rref(mat):

    # For each column, look for 
    # non-zero elements in bottom n rows (decremented each pivot)

    pivots = []
    for col in range(len(mat[0]) - 1):

        row = len(pivots)
        old_row = -1
        for r in range(row, len(mat)):
            if mat[r][col] != 0:
                old_row = r
                break
        if old_row == -1:
            continue

        pivots.append(col)

        # move row to row == len(pivots)
        mat[old_row], mat[row] = mat[row], mat[old_row]

        # set row pivot to 1
        div_row(mat, row, mat[row][col])

        # loop through other rows and clear the col
        for r in range(len(mat)):
            if r == row or mat[r][col] == 0:
                continue
            sub_row(mat, row, r, mat[r][col])
    
    return mat





# Functions for finding solution from reduced matrix
def find_var_bounds(targets, buttons):
    return [min([targets[x] for x in button]) for button in buttons]

def gen_assignments(vars, var_bounds):
    if len(vars) == 0:
        return

    assn = [0] * len(vars)
    yield assn
    while True:
        assn[0] += 1

        # Fix looping
        i = 0
        while True:
            if assn[i] == var_bounds[vars[i]] + 1:
                if i == len(vars) - 1:
                    return

                assn[i] = 0
                assn[i + 1] += 1
                i += 1
            else:
                break

        yield assn



def find_min_sol(r_mat, var_bounds) -> int:
    # Identify pivots & free vars
    for i in range(len(r_mat)):
        for j in range(len(r_mat[0])):
            r_mat[i][j] = round(r_mat[i][j])

    pivots = []
    try:
        pivots = [row.index(1) for row in r_mat if any(row)]
    except:
        for r in r_mat:
            print(r)
        exit()

    free_vars = [x for x in range(len(r_mat[0]) - 1) if x not in pivots]

    # Get vector generator
    def get_vect(ls):
        vect = []
        for i in range(len(r_mat[0]) - 1):
            if i in pivots:
                row = r_mat[pivots.index(i)]
                n = row[-1]
                for i in range(len(free_vars)):
                    var = free_vars[i]
                    n -= ls[i] * row[var]
                vect.append(n)

            else:
                vect.append(ls[free_vars.index(i)])

        return vect

    # For each variable assignment
    min_presses = sum(var_bounds) * 2 # just to be safe, idk what I'm doing
    for assn in gen_assignments(free_vars, var_bounds):
        vect = get_vect(assn)
        # print(assn)
        if any([x < 0 for x in vect]):
            continue
        presses = round(sum(vect))
        if presses < min_presses:
            # print(assn, vect, presses)
            min_presses = presses

    return min_presses



# test_mat = [
#     [1, 0, 0, 1, 0, -1, 2],
#     [0, 1, 0, 0, 0,  1, 5],
#     [0, 0, 1, 1, 0, -1, 1],
#     [0, 0, 0, 0, 1,  1, 3]
# ]

# test_ind = 1
# test_mat = rref(matrices[test_ind])

# bounds = find_var_bounds(machines[test_ind][0], machines[test_ind][1])

# # for r in test_mat:
# #     print(r)
# print(find_min_sol(test_mat, bounds))


# exit()

# Put it all together
total = 0
for i in range(len(matrices)):
    mat = matrices[i]
    targets, buttons = machines[i]

    r_mat = rref(mat)
    bounds = find_var_bounds(targets, buttons)
    min_sol = find_min_sol(r_mat, bounds)
    total += min_sol
    print(min_sol)

print("Total:", total)

