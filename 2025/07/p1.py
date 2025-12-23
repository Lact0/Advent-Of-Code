
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

beams = {inp[0].index("S")}
splits = 0
for i in range(1, len(inp)):
    row = inp[i]
    new_beams = set()

    for beam in beams:
        if row[beam] == '^':
            splits += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        else:
            new_beams.add(beam)
    beams = new_beams

print(splits)