def find_highest_joltage(line):
    joltage, line = line[:12], line[12:]
    while line:
        current, line = line[0], line[1:]
        index_to_remove = -1
        for i in range(1, 12):
            if joltage[i] > joltage[i-1]:
                index_to_remove = i-1
                break
        if index_to_remove != -1:
            joltage = joltage[:index_to_remove] + joltage[index_to_remove + 1:] + current
        else:
            if current > joltage[-1]:
                joltage = joltage[:-1] + current

    return int(joltage)

with open("Day3/data.txt", "r") as file:
    lines = file.read().splitlines()

total_joltage = 0

for line in lines:
    total_joltage += find_highest_joltage(line)

print(total_joltage)