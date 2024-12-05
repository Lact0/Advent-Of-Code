inp = []
with open("Day 2/bigTest.txt", "r") as file:
    for line in file:
        inp.append(line.split())

sum = 0
for game in inp:
    min = {'blue': 0, 'green': 0, 'red': 0}
    i = 2
    for i in range(2, len(game)):
        if game[i].isdigit():
            col = game[i + 1].strip(",").strip(";")
            if min[col] < int(game[i]):
                min[col] = int(game[i])
    sum += min['blue'] * min['green'] * min['red']
print(sum)