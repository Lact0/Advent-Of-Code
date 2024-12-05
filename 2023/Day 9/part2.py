inp = []
with open("Day 9/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

hists = [[int(x) for x in y.split()] for y in inp]

total = 0

for hist in hists:
    pyr = [hist]
    while not (max(last := pyr[-1]) == min(last) and max(last) == 0):
        pyr.append([last[x + 1] - last[x] for x in range(len(last) - 1)])
    
    n = sum([pyr[i][0] * (1 - 2 * (i % 2 == 1)) for i in range(len(pyr))])
    total += n

print(total)
