""" Day 10 of Advent of Code 2024"""
with open("puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

def path_hunter(rows: list, i: int, j: int) -> list:
    """ Recursively explore trail to trailhead """
    trailheads = []
    for y, x in [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]:
        if y < 0 or x < 0 or y >= len(rows) or x >= len(rows[0]):
            continue
        if rows[y][x] == 9 and rows[i][j] == 8:
            trailheads.append((y,x))
        elif rows[y][x] == rows[i][j] + 1:
            trailheads += path_hunter(rows, y, x)
    return trailheads

def calculate_trailheads(data: str, rating: bool = False) -> int:
    """ Calculate number of trailheads from each start location """
    rows = [[int(n) for n in row] for row in data.split("\n")]
    trailheads = 0
    for i, row in enumerate(rows):
        for j, _ in enumerate(row):
            if row[j] == 0:
                if rating:
                    trailheads += len(path_hunter(rows, i, j))
                else:
                    trailheads += len(set(path_hunter(rows, i, j)))
    return trailheads

# Part 1
assert calculate_trailheads(test_data) == 36

print(f"Part 1: {calculate_trailheads(input_data)}")

# Part 2
assert calculate_trailheads(test_data, rating=True) == 81

print(f"Part 2: {calculate_trailheads(input_data, rating=True)}")
