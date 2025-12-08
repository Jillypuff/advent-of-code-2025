class Coords():
    def __init__(self, y, x):
        self.y = y
        self.x = x

def memoize(func):
    cache = {}
    def wrapper(coord):
        key = (coord.y, coord.x)
        if key not in cache:
            cache[key] = func(coord)
        return cache[key]
    return wrapper

@memoize
def recursive_find_split(coord) -> int:
    y = coord.y
    x = coord.x
    for i in range(y, height):
        if lines[i][x] == splitter:
            return recursive_find_split(Coords(i + 1, x - 1)) + recursive_find_split(Coords(i + 1, x + 1))
    return 1

with open("Day7/data.txt", "r") as file:
    lines = file.read().splitlines()

start = Coords(0, lines[0].index("S"))
splitter, height = "^", len(lines)
print(recursive_find_split(start))