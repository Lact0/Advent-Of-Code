inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

reports = [[int(j) for j in i.split()] for i in inp]


def checkSafe(report):
    prev = report[1] - report[0]
    if abs(prev) < 1 or abs(prev) > 3:
        return False
    
    for i in range(len(report) - 1):
        cur = report[i + 1] - report[i]
        if cur * prev <= 0:
            return False
        if abs(cur) < 1 or abs(cur) > 3:
            return False
    return True


total = 0
for report in reports:
    safe = checkSafe(report)
    for i in range(len(report)):
        safe |= checkSafe(report[:i] + report[i + 1:])
    if safe:
        total += 1

print(total)

# Finished at 12:11 AM