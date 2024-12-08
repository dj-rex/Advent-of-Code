""" Day 8 of Advent of Code 2024"""
from itertools import combinations
with open("aoc_2024/day_8/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_8/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

# Part 1
def get_antenna_types(data: str) -> list:
    """ Get antenna types from input data """
    antenna_types = list(set(data))
    antenna_types.remove(".")
    antenna_types.remove("\n")
    return antenna_types

def calculate_antinodes(data: str, t_nodes: bool = False) -> int:
    """ Calculate the number of antinodes """
    antenna_locs = {_: [] for _ in get_antenna_types(data)}
    lines = data.split("\n")
    # Find locations of antennas
    for irow, row in enumerate(lines):
        for icol, char in enumerate(row):
            if char == ".":
                continue
            antenna_locs[char].append([irow, icol])
    # For each antenna type, find signal overlaps
    overlaps = set()
    for locs in antenna_locs.values():
        for loc_a, loc_b in combinations(locs, r=2):
            dy, dx = loc_b[0] - loc_a[0], loc_b[1] - loc_a[1]
            n = -1 if t_nodes else 0
            while True:
                n+=1
                x1, y1 = loc_a[1]-dx*n, loc_a[0]-dy*n
                x2, y2 = loc_b[1]+dx*n, loc_b[0]+dy*n
                overlaps.add(f"{y1},{x1}")
                overlaps.add(f"{y2},{x2}")
                if not t_nodes:
                    break
                if not (0 <= x1 < len(lines[0]) or 0 <= x2 < len(lines[0]) or 0 <= y1 < len(lines) or 0 <= y2 < len(lines)):
                    break
    # clean up out of bounds
    out_of_bounds=set()
    for overlap in overlaps:
        irow, icol = overlap.split(",")
        if int(irow) < 0 or int(irow) > len(lines)-1 or int(icol) < 0 or int(icol) > len(lines[0])-1:
            out_of_bounds.add(overlap)
    return len(overlaps-out_of_bounds)

assert calculate_antinodes(test_data) == 14

print(f"Part 1: {calculate_antinodes(input_data)}")

# Part 2
assert calculate_antinodes(test_data, t_nodes=True) == 34

print(f"Part 2: {calculate_antinodes(input_data, t_nodes=True)}")
