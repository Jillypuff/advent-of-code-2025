def combine_ranges(new_range):
    new_start, new_end = map(int, new_range.split("-"))
    for index, range in enumerate(combined_ranges):
        start, end = map(int, range.split("-"))
        if start <= new_start <= end:
            combined_ranges[index] = f"{start}-{max(new_end, end)}"
            return
        elif start <= new_end <= end:
            combined_ranges[index] = f"{min(new_start, start)}-{end}"
            return
        elif new_start < start and new_end > end:
            combined_ranges[index] = f"{new_start}-{new_end}"
            return
    combined_ranges.append(new_range)

def count_fresh_ids(range):
    start, end = map(int, range.split("-"))
    return end - start + 1

with open("Day5/data.txt", "r") as file:
    lines = file.read().splitlines()

separator = lines.index("")
fresh_ranges = lines[:separator]
combined_ranges = []

while True:
    for fresh_range in fresh_ranges:
        combine_ranges(fresh_range)
    if fresh_ranges == combined_ranges:
        break
    fresh_ranges = combined_ranges.copy()
    combined_ranges = []

fresh_ingredient_ids = 0
for combined_range in combined_ranges:
    fresh_ingredient_ids += count_fresh_ids(combined_range)

print(fresh_ingredient_ids)