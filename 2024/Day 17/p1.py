inp = []
with open("s2.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))

A = int(inp[0].split(" ")[2])
B = int(inp[1].split(" ")[2])
C = int(inp[2].split(" ")[2])

instructions = [int(x) for x in inp[4].split(" ")[1].split(",")]
comb = {0: (lambda : 0), 1: (lambda : 1), 2: (lambda : 2), 3: (lambda: 3), 4: (lambda : A), 5: (lambda : B), 6: (lambda : C)}


output = []

ip = 0
while ip < len(instructions):
    opcode = instructions[ip]
    operand = instructions[ip+1]

    jumped = False

    match opcode:
        case 0:
            A //= (2 ** comb[operand]())
        case 1:
            B ^= operand
        case 2:
            B = comb[operand]() % 8
        case 3:
            if A != 0:
                jumped = True
                ip = operand
        case 4:
            B ^= C
        case 5:
            output.append(comb[operand]() % 8)
        case 6:
            B = A // (2 ** comb[operand]())
        case 7:
            C = A // (2 ** comb[operand]())


    if not jumped: ip += 2

output = [str(x) for x in output]
print(",".join(output))