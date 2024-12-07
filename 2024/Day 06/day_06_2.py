import copy
def next_pos(row, col, char):
    if char == '^':
        return row - 1, col
    elif char == '>':
        return row, col + 1
    elif char == '<':
        return row, col - 1
    else:
        return row + 1, col

def next_guard_char(char):
    if char == '^':
        return '>'
    elif char == '>':
        return 'v'
    elif char == 'v':
        return '<'
    elif char == '<':
        return '^'
    
def is_loop(grid, guard_char2, already_known, pos):
    rows = len(grid)
    cols = len(grid[0])
    new_pos = pos
    old_pos = pos
    guard_char = guard_char2
    while True:
        if new_pos not in already_known:
            already_known[new_pos] = []
        if guard_char in already_known[new_pos]:
            return True
        else:
            already_known[new_pos].append(guard_char)
        old_pos = new_pos
        new_pos = next_pos(new_pos[0], new_pos[1], guard_char)
        next_row = new_pos[0]
        next_col = new_pos[1]

        if next_row >= rows or next_row < 0 or next_col >= cols or next_col < 0:
            # print('false!')
            return False
        else:
            at_next_pos = grid[next_row][next_col]
            if at_next_pos == '#' or at_next_pos == 'O':
                guard_char = next_guard_char(guard_char)
                new_pos = old_pos

with open('b.txt') as f:
    lines = f.readlines()
    rows = len(lines) - 1
    cols = len(lines[0])

    grid = []

    guard_row = 0
    guard_col = 0
    for i in range(len(lines) - 1):
        line = lines[i].rstrip()
        grid.append([' ' for i in range(len(line))])
        for c in range(len(line)):
            if line[c] == '#':
                grid[i][c] = '#'
            elif line[c] == '.':
                grid[i][c] = '.'
            if line[c] == '^':
                grid[i][c] = '.'
                guard_row = i
                guard_col = c
                # break

    guard_pos = guard_row, guard_col 
    new_pos = guard_pos
    visited = []
    valid_obstacles = 0
    guard_char = '^'
    already_known = {}
    obstacle_pos = []
    already_known[new_pos] = [guard_char]
    while True:
        old_pos = new_pos
        new_pos = next_pos(new_pos[0], new_pos[1], guard_char)
        next_row = new_pos[0]
        next_col = new_pos[1]

        if next_row >= rows or next_row < 0 or next_col >= cols or next_col < 0:
            break
        else:
            at_next_pos = grid[next_row][next_col]
            if at_next_pos == '#':
                guard_char = next_guard_char(guard_char)
                new_pos = old_pos
                continue
            elif new_pos not in obstacle_pos:
                try_grid = copy.deepcopy(grid)
                try_grid[next_row][next_col] = 'O'

                if is_loop(try_grid, next_guard_char(guard_char), copy.deepcopy(already_known), old_pos):
                    obstacle_pos.append(new_pos)
                    valid_obstacles += 1
    print(valid_obstacles)