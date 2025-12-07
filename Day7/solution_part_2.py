class Coords():
    def __init__(self, y, x):
        self.y = y
        self.x = x

def find_split(y, x):
    print(y)
    for i in range(y, height - 1):
        if lines[i][x] == splitter:
            return Coords(i, x)
    return None

with open("Day7/data.txt", "r") as file:
    lines = file.read().splitlines()
#lines[y][x]

start = Coords(0, lines[0].index("S"))
tachyon_particles = []
tachyon_particles.append(start)
splits, splitter, height = 0, '^', len(lines)
while tachyon_particles:
    current = tachyon_particles.pop()
    split_coord = find_split(current.y, current.x)
    print(len(tachyon_particles))
    if split_coord:
        splits += 1
        tachyon_particles.append(Coords(split_coord.y - 1, split_coord.x - 1))
        tachyon_particles.append(Coords(split_coord.y - 1, split_coord.x + 1))

print(splits)