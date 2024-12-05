inp = []
with open("Day 6/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

times = [int(x) for x in inp[0].split()[1:]]
dist = [int(x) for x in inp[1].split()[1:]]
races = [[times[i], dist[i]] for i in range(len(times))]

margin = 1
for time, bestDist in races:
    numWays = 0
    for i in range(time + 1):
        numWays += i * (time - i)> bestDist
    margin *= numWays

print(margin)