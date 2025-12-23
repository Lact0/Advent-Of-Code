
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

beams = {inp[0].index("S"): 1}
splits = 0

def add_to_beams(beams, beam, n):
    if beam in beams:
        beams[beam] += n
    else:
        beams[beam] = n

for i in range(1, len(inp)):
    row = inp[i]
    new_beams = {}

    for beam in beams.keys():
        n = beams[beam]
        if row[beam] == '^':
            splits += 1
            add_to_beams(new_beams, beam - 1, n)
            add_to_beams(new_beams, beam + 1, n)
        else:
            add_to_beams(new_beams, beam, n)
    beams = new_beams

s = 0
for key in beams.keys():
    s += beams[key]
print(s)