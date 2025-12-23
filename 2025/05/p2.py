
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))
           
ranges = []
for row in inp:
    if row == "":
        break
    ranges.append([int(x) for x in row.split("-")])

ranges.sort(key=lambda x: x[0])
print(ranges)

total = 0
start = ranges[0][0]
end = ranges[0][1]
for new_start, new_end in ranges[1:]:
    if new_start > end:
        total += end - start + 1
        start, end = new_start, new_end 
    else:
        end = max(end, new_end)       

total += end - start + 1
print(total)