inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))


instructions = [int(x) for x in inp[4].split(" ")[1].split(",")]
comb = {0: (lambda : 0), 1: (lambda : 1), 2: (lambda : 2), 3: (lambda: 3), 4: (lambda : A), 5: (lambda : B), 6: (lambda : C)}

prevLen = 0

def calcIter(skely):
    total = 0
    for i in range(len(skely)):
        total += (8 ** i) * skely[i]
    return total


iterSkely = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
iterPointer = 15


while True:

    # Reset computer
    iteration = calcIter(iterSkely)
    A = iteration
    B = 0
    C = 0
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

    # If the current end we are trying to match matches matches
    if output[iterPointer:] == instructions[iterPointer:]:
        print("FOUND DIGIT", iterPointer, output, iterSkely)
        iterPointer -= 1
    else:
        iterSkely[iterPointer] += 1


    if output == instructions: break

    # Current thing is wrong, backtrack
    if iterSkely[iterPointer] >= 8:
        print("BACKTRACKING AT DIGIT", iterPointer)
        iterSkely[iterPointer] = 0
        iterPointer += 1
        iterSkely[iterPointer] += 1




print("CORRECT ITERATION:", calcIter(iterSkely))

#Highest: 30700000 (probably 211106217100000)