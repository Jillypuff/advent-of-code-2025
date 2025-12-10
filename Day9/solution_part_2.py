class Coord():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y

with open("Day8/data.txt", "r") as file:
    lines = file.read().splitlines()

coords = []
for line in lines:
    x, y = map(int, line.split(","))
    coords.append(Coord(x, y))