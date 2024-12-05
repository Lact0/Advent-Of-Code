inp = []
with open("Day 4/fullTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

data = []
for row in inp:
    sp = row.split("|")
    data.append([sp[0].split()[2:], sp[1].split()])

score = 0
for winners, nums in data:
    wins = 0
    for n in nums:
        if n in winners:
            wins += 1
    score += 2 ** (wins - 1) if wins else 0
print(score)