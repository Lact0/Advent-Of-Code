inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))
l1 = [int(i.split(" ")[0]) for i in inp]
l2 = [int(i.split(" ")[3]) for i in inp]

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])

print(sum)