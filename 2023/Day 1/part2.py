inp = []
with open("Day 1/bigTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

#THIS SOLUTION IS ABSOLUTELY DISGUSTING I KNOW

numsS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numsD = [str(x) for x in range(1, 10)]

sum = 0
for string in inp:
    first = [0, len(string)]
    last = [0, -1]
    for s in numsS:
        if not string.count(s):
            continue
        ind = string.index(s)
        if(ind < first[1]):
            first = [numsS.index(s) + 1, ind]
        ind = string.rindex(s)
        if(ind > last[1]):
            last = [numsS.index(s) + 1, ind]
    for s in numsD:
        if not string.count(s):
            continue
        ind = string.index(s)
        if(ind < first[1]):
            first = [int(s), ind]
        ind = string.rindex(s)
        if(ind > last[1]):
            last = [int(s), ind]
    print(first, last, string)
    sum += int(str(first[0]) + str(last[0]))
print(sum)
