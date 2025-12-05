def check_freshness(ingredient):
    for fresh_range in fresh_ranges:
        start, end = fresh_range.split("-")
        if int(start) <= int(ingredient) <= int(end):
            return True
    return False

with open("Day5/data.txt", "r") as file:
    lines = file.read().splitlines()

separator = lines.index("")
fresh_ranges, ingredients = lines[:separator], lines[separator + 1:]

fresh_ingredients = 0
for ingredient in ingredients:
    if check_freshness(ingredient):
        fresh_ingredients += 1

print(fresh_ingredients)