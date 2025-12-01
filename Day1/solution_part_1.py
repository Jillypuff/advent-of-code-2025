def turn_dial(position, line):
    direction, rotations = split_line(line)
    position = position + rotations if direction == "R" else position - rotations
    return position % 100

def split_line(line):
    return line[0], int(line[1:])

with open("Day1/data.txt", "r") as file:
    lines = file.read().splitlines()

position = 50
clicks = 0

for line in lines:
    position = turn_dial(position, line)
    if position == 0:
        clicks += 1

print(clicks)