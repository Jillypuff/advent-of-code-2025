def validate_id(id):
    length = len(id)
    if length % 2 != 0:
        return True
    
    half_length = int(length / 2)
    if id[half_length:] == id[:half_length]:
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