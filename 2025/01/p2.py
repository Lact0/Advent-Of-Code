
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

dirs = [(1 if s[0] == "R" else -1) for s in inp]
nums = [int(s[1:]) for s in inp]

count = 0
dial = 50
for i in range(len(inp)):
    for j in range(nums[i]):
        dial = (dial + dirs[i]) % 100
        if dial == 0:
            count += 1

print(count)