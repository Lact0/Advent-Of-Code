
inp = []
with open("b.txt", "r") as file:
    for row in file:
        inp.append(row.strip("\n"))
inp = [tuple([int(x) for x in y.split(',')]) for y in inp]

conn = []
circuits = {inp[x]:x for x in range(len(inp))}

def dist(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2

sorted_conns = []
for i in range(len(inp)):
    for j in range(i+1, len(inp)):
        sorted_conns.append((inp[i], inp[j]))
sorted_conns.sort(key=lambda x: dist(x[0], x[1]))

def set_circuit(old, new):
    old_n = circuits[old]
    new_n = circuits[new]
    for key in circuits:
        if circuits[key] == old_n:
            circuits[key] = new_n

n_conn = 1000
i = 0
while len(conn) < n_conn:
    c0, c1 = sorted_conns[i]
    i += 1

    conn.append((c0, c1))
    set_circuit(c0, c1)

comp_circuits = [0 for i in range(len(inp))]
for key in circuits:
    comp_circuits[circuits[key]] += 1
comp_circuits.sort(reverse=True)
print(comp_circuits[0] * comp_circuits[1] * comp_circuits[2])
    


