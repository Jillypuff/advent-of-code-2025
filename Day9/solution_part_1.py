class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_area(coord1, coord2):
    return (abs(coord1.x - coord2.x) + 1) * (abs(coord1.y - coord2.y) + 1)

with open("Day9/data.txt", "r") as file:
    lines = file.read().splitlines()

coords = []
for line in lines:
    x, y = map(int, line.split(","))
    coords.append(Coord(x, y))

areas = []
for i, coord in enumerate(coords):
    for j in range(i + 1, len(coords)):
        areas.append(calculate_area(coord, coords[j]))

print(max(areas))