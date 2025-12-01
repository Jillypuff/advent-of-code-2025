def turn_dial(position, line, clicks):
    direction, rotations = line[0], int(line[1:])
    while rotations > 99:
        clicks += 1
        rotations -= 100

    if direction == "R":
        if position + rotations > 99:
            clicks += 1
        position += rotations
    else:
        if position != 0 and position - rotations <= 0:
            clicks += 1
        position -= rotations

    return position % 100, clicks

with open("Day1/data.txt", "r") as file:
    lines = file.read().splitlines()

position = 50
clicks = 0

for line in lines:
    position, clicks = turn_dial(position, line, clicks)

print(clicks)