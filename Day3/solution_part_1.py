def find_highest_joltage(line):
    first, second, line = int(line[0]), int(line[1]), line[2:]
    while line:
        current = int(line[0])
        if second > first:
            first, second = second, current
        elif current > second:
            second = current
        if first + second == 18:
            return 99
        line = line[1:]

    return int(str(first) + str(second))


with open("Day3/data.txt", "r") as file:
    lines = file.read().splitlines()

total_joltage = 0

for line in lines:
    total_joltage += find_highest_joltage(line)

print(total_joltage)