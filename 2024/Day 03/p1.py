inp = ''
with open("b.txt", "r") as file:
    for row in file:
        inp += row.strip("\n")

instr = []
cur = ''
for c in inp:
    if c == 'm' and cur == '':
        cur += c
    elif c == 'u' and cur == 'm':
        cur += c
    elif c == 'l' and cur == 'mu':
        cur += c
    elif c == '(' and cur == 'mul':
        cur += c
    elif c.isdigit() and len(cur) > 0 and cur[-1] in '(0123456789,':
        cur += c
    elif c == ',' and len(cur) > 0 and cur[-1].isdigit() and (',' not in cur):
        cur += c
    elif c == ')' and len(cur) > 0 and cur[-1].isdigit():
        cur += c
        instr.append(cur)
        cur = ''
    else:
        cur = ''

sm = 0
for i in instr:
    p1, p2 = i.split(",")
    sm += int(p1[4:]) * int(p2[:-1])

print(sm)
    
# 12:12 AM