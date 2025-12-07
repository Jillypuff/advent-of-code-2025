with open("Day7/data.txt", "r") as file:
    lines = file.read().splitlines()

beam_indexes = {lines[0].index("S")}
splits, splitter, height = 0, '^', len(lines)
print(type(beam_indexes))

for i in range(0, height):
    temp_set = beam_indexes.copy()
    for index in beam_indexes:
        if lines[i][index] == splitter:
            splits += 1
            temp_set.remove(index)
            temp_set.update({index -1, index + 1})
    beam_indexes = temp_set.copy()

print(splits)