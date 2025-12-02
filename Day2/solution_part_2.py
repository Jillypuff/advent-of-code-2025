def compare_values(id, sequence_size):
    target_sequence, id = id[:sequence_size], id[sequence_size:]
    while id:
        next_sequence, id = id[:sequence_size], id[sequence_size:]
        if target_sequence != next_sequence:
            return False
        
    return True

def validate_id(id):
    length = len(id)
    half_length = int(length / 2)
    for i in range(1, half_length + 1):
        if length % i == 0:
            repeated_values = compare_values(id, i)
            if repeated_values:
                return False

    return True

def validate_id_range(id_range):
    start, end = map(int, id_range.split("-"))
    invalid_id_sum = 0
    for id in range(start, end + 1):
        valid = validate_id(str(id))
        if not valid:
            invalid_id_sum += id

    return invalid_id_sum

with open("Day2/data.txt", "r") as file:
    data = file.read()

id_ranges = data.split(",")
invalid_id_sum = 0

for id_range in id_ranges:
    invalid_id_sum += validate_id_range(id_range)

print(invalid_id_sum)