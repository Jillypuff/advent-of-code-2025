class Coords():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Distance():
    def __init__(self, coord1, coord2, distance):
        self.coord1 = coord1
        self.coord2 = coord2
        self.distance = distance

def calculate_vector_distance(v, w) -> float:
    return ((v.x - w.x) ** 2 + (v.y - w.y) ** 2 + (v.z - w.z) ** 2) ** 0.5

with open("Day8/data.txt", "r") as file:
    lines = file.read().splitlines()

coords = []
for line in lines:
    x,y,z = map(int, line.split(","))
    coords.append(Coords(x, y, z))

distances = []
for index, coord in enumerate(coords):
    for i in range(index + 1, len(coords)):
        distances.append(Distance(coord, coords[i], calculate_vector_distance(coord, coords[i])))
distances.sort(key=lambda x: x.distance)

circuits = []
for i in range(0, 1000):
    new_circuit = [distances[i].coord1, distances[i].coord2]
    a, b = -1, -1
    for j, circuit in enumerate(circuits):
        if new_circuit[0] in circuit:
            a = j
        if new_circuit[1] in circuit:
            b = j
    if a != -1 and b != -1:
        if a == b:
            continue
        circuits[a].extend(circuits.pop(b))
    elif a != -1 and b == -1:
        circuits[a].append(new_circuit[1])
    elif a == -1 and b != -1:
        circuits[b].append(new_circuit[0])
    else:
        circuits.append(new_circuit)
circuits.sort(key=lambda x: len(x), reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))