inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

inp = [int(x) for x in inp[0]]
# inp = [3, 5, 5, 2, 1]
indices = [sum(inp[:i]) for i in range(len(inp))]
size = sum(inp)

# [id, count]
ids = [[i, inp[int(i)*2]] for i in range(int(len(inp) / 2)+1)]

# Specifies where the free spaces are in drive
# [start, length]
free = [[indices[i*2+1], inp[i*2+1]] for i in range(int(len(inp) / 2))]
# print(free)
# print(ids)

# We want to take from teh back of ids, and put them in the first free that fits.
# Then, segment that free, or delete it.
# We must then add to the "final" pile, where we have the final coords of all indices.

# [id, startIndex, length]
finalPositions = []
while len(ids) > 0:

    # Get id, length and index of last file
    id, length = ids.pop()
    index = indices[len(ids)*2]

    # loop through free spaces
    # keep track of if a successful insert happened
    inserted = False
    for i in range(len(free)):

        freeIndex, freeLength = free[i]
        if freeIndex > index:
            break


        if freeLength == length:
            free = free[:i] + free[i+1:]
            finalPositions.append([id, freeIndex, length])
            inserted = True
        if freeLength > length:
            newFragment = [freeIndex + length, freeLength - length]
            free = free[:i] + [newFragment] + free[i+1:]
            finalPositions.append([id, freeIndex, length])
            inserted = True

        if inserted:
            break

    # handle no insert
    if not inserted:
        finalPositions.append([id, index, length])



# Go through all files and add everything
sm = 0
for id, startIndex, length in finalPositions:
    print(id, startIndex, length)
    for i in range(length):
        sm += id * (startIndex + i)
print(sm)

# 12:58 AM