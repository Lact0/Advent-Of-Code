
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [tuple(int(x) for x in y.split(',')) for y in inp]

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def point_crosses_line(p, l1, l2):
    lx1, ly1 = l1
    lx2, ly2 = l2
    x, y = p

    if lx1 == lx2: 
        # vertical case
        if x < lx1:
            return False
        return y <= max(ly1, ly2) and y > min(ly1, ly2)
    return False

lines = []
for i in range(len(inp)):
    lines.append((inp[i], inp[(i + 1) % len(inp)]))

def point_on_line(p, l1, l2):
    x, y = p
    x_in = x <= max(l1[0], l2[0]) and x >= min(l1[0], l2[0])
    y_in = y <= max(l1[1], l2[1]) and y >= min(l1[1], l2[1])
    if x_in and y_in:
        return True
    return False

def point_inside(p):
    n = 0
    for l1, l2 in lines:
        if point_on_line(p, l1, l2):
            return True
        if point_crosses_line(p, l1, l2):
            n += 1
    return n % 2 == 1

def point_in_rect(x1, y1, x2, y2, x, y):
    return x > x1 and x < x2 and y > y1 and y < y2

def line_crosses_rect(x1, y1, x2, y2, l1, l2):
    l1x, l2x = min(l1[0], l2[0]), max(l1[0], l2[0])
    l1y, l2y = min(l1[1], l2[1]), max(l1[1], l2[1])

    if point_in_rect(x1, y1, x2, y2, l1[0], l1[1]):
        return True
    if point_in_rect(x1, y1, x2, y2, l2[0], l2[1]):
        return True

    if l1x == l2x:
        # vertical line
        return (l1x > x1 and l1x < x2) and (l1y <= y1 and l2y >= y2)

    else:
        # horizontal
        return (l1y > y1 and l1y < y2) and (l1x <= x1 and l2x >= x2)

def valid_rectangle(x1, y1, x2, y2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for l1, l2 in lines:
        if line_crosses_rect(x1, y1, x2, y2, l1, l2):
            return False
    return True

max_area = 0
for i in range(len(inp)):
    print(i)
    for j in range(i + 1, len(inp)):
        x1, y1 = inp[i]
        x2, y2 = inp[j]
        if not valid_rectangle(x1, y1, x2, y2):
            continue

        a = area(inp[i], inp[j])
        if a > max_area:
            max_area = a

print(max_area)