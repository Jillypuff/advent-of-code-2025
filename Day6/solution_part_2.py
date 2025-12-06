def parse_data(previous, current):
    subset = []
    for j in range(current - 1, previous - 1, - 1):
        column = ''
        for k in range(0,4):
            if lines[k][j] != ' ':
                column += lines[k][j]
        if column != '':
            subset.append(int(column))
    return subset

def calculate_sum(data, operator):
    if operator == '+':
        return sum(data)
    if operator == '*':
        result = data[0]
        for i in range(1, len(data)):
            result *= data[i]
        return result

with open ("Day6/data.txt", "r") as file:
    lines = file.read().splitlines()

rows = len(lines[0])
total_sum = 0

previous, current = 0, 0
for i in range(1, rows):
    if lines[4][i] in ('+', '*'):
        total_sum += calculate_sum((parse_data(previous, i)), lines[4][previous])
        previous = i
else:
    total_sum += calculate_sum((parse_data(previous, rows)), lines[4][previous])

print(total_sum)