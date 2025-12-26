
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [x.split() for x in inp]

# A machines is: (size, need_on, buttons)
# where need_on is a list of ints (positions on)
# and buttons is a list of buttons, which are lists of ints
machines = []
for row in inp:
    need_on = []
    for i in range(1, len(row[0]) - 1):
        if row[0][i] == '#':
            need_on.append(i - 1)

    buttons = []
    for i in range(1, len(row) - 1):
        buttons.append([int(x) for x in row[i][1:-1].split(',')])

    machines.append((len(row[0]) - 2, need_on, buttons))

def is_sol(size, need_on, buttons, n):
    # if n == 10:
    #     print(size, need_on, buttons, list(bin(n))[2:])
    pattern = list(bin(n))[2:]
    pattern.reverse()
    lights = [False for i in range(size)]
    for i in range(len(pattern)):
        if pattern[i] == '0':
            continue
        for l in buttons[i]:
            lights[l] = not lights[l]
    for i in range(len(lights)):
        if lights[i] != (i in need_on):
            return False
    return True

def count_flips(n):
    return list(bin(n))[2:].count('1')

s = 0
for size, need_on, buttons in machines:
    smallest = 100000000000000000000000000
    for i in range(2 ** len(buttons)):
        if is_sol(size, need_on, buttons, i):
            # print(list(bin(i))[2:])
            if count_flips(i) < smallest:
                smallest = count_flips(i)
    # print(smallest)
    s += smallest
print(s)