inp = []
with open("s.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [int(x) for x in inp[0]]
indices = [sum(inp[:i+1]) for i in range(len(inp))]

totalFileSize = 0
for i in range(len(inp)):
    if i % 2 == 0:
        totalFileSize += inp[i]

#print(inp)
#print(indices)

# [id, count]
ids = [[i, inp[int(i)*2]] for i in range(int(len(inp) / 2)+1)]

sm = 0
curIndex = 0
for i in range(totalFileSize):
    if curIndex % 2 == 0:
        #print(int(curIndex / 2))
        sm += i * ids[0][0]
        ids[0][1] -= 1
        if ids[0][1] == 0:
            ids = ids[1:]
            curIndex += 1
    else:
        #print(ids[-1][0])
        sm += i * ids[-1][0]
        ids[-1][1] -= 1
        if ids[-1][1] == 0:
            ids = ids[:-1]

    #update curINdex if required
    if i + 1 == indices[curIndex]:
        curIndex += 1
print(sm)

# 12:23 AM