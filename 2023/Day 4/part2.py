inp = []
with open("Day 4/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

data = []
for row in inp:
    sp = row.split("|")
    data.append([sp[0].split()[2:], sp[1].split()])

numCards = [1] * len(data)
for i in range(len(data)):
    winners, nums = data[i]
    wins = 1
    for n in nums:
        if n in winners:
            numCards[i + wins] += numCards[i]
            wins += 1
print(sum(numCards))