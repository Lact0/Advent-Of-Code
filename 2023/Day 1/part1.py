inp = []
with open("Day 1/bigTest.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

sum = 0
for string in inp:
    first = None
    last = None
    for s in string:
        if(s.isdigit()):
            first = first if first is not None else s
            last = s
    sum += int(first + last)
print(sum)
