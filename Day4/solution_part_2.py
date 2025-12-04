def check_borders(x, y):
    return left <= x <= right and top <= y <= bottom

def count_neighbors(dataset, x, y):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if check_borders(x + i, y + j):
                if dataset[x + i][y + j] == roll:
                    neighbors += 1
    return neighbors

with open("Day4/data.txt", "r") as file:
    lines = file.read().splitlines()

dataset = []
for line in lines:
    chars = list(line)
    dataset.append(chars)
new_dataset = dataset

top, left, right, bottom = 0, 0, len(dataset[0]) - 1, len(dataset) - 1
roll, empty = "@", "."
forklift_accessable_rolls = 0

changes = True
while changes:
    changes = False
    for x in range(0, len(dataset)):
        for y in range(0, len(dataset[x])):
            if dataset[x][y] != roll:
                continue
            neighbors = count_neighbors(dataset, x, y)
            if neighbors < 4:
                new_dataset[x][y] = empty
                changes = True
                forklift_accessable_rolls += 1
    dataset = new_dataset

print(forklift_accessable_rolls)