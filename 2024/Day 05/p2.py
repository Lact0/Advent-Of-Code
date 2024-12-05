inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

b = inp.index('')
rules = [[int(x) for x in rule.split('|')] for rule in inp[:b]]
lists = [[int(x) for x in l.split(',')] for l in inp[b+1:]]


dic = {}
for rule in rules:
    if rule[0] not in dic.keys():
        dic[rule[0]] = []
    dic[rule[0]].append(rule[1])

sm = 0
for l in lists:

    valid = True
    for i in range(len(l)):
        n1 = l[i]
        if n1 not in dic.keys(): continue

        tempI = i
        for n2 in dic[n1]:
            if n2 in l[:tempI]:
                valid = False
                ind = l.index(n2)
                l = l[:ind] + [n1] + l[ind:tempI] + l[tempI + 1:]
                tempI = ind

    if not valid:
        print(l)
        sm += l[int(len(l) / 2)]

print(sm)

# 12:20 AM