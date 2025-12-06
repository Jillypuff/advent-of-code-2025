with open ("Day6/data.txt", "r") as file:
    lines = file.read().splitlines()

columns = len(lines)

data = []
for i in range(0, columns):
    data.append(lines[i].split())

rows = len(data[0])
total_sum = 0

for i in range(0, rows):
    operator = data[-1][i]
    if operator == '+':
        sum = 0
        for j in range(0, columns - 1):
            sum += int(data[j][i])
        total_sum += sum
    elif operator == '*':
        sum = int(data[0][i])
        for j in range(1, columns - 1):
            sum *= int(data[j][i])
        total_sum += sum

print(total_sum)