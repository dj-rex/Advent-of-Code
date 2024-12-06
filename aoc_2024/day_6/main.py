""" Day Six of Advent of Code 2024"""
from copy import deepcopy
with open("aoc_2024/day_6/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_6/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

# Part 1
def next_pos(rows:list, old_pos:str, old_dir:str) -> str:
    """ Find the next position based on current position and direction """
    x, y = old_pos.split(",")
    if x == "8" and y == "6":
        pass
    if old_dir == "up":
        if int(y) == 0:
            return "end;"
        if rows[int(y)-1][int(x)] in [".", "^"]:
            return f"{int(x)},{int(y)-1};up"
        else:
            return next_pos(rows, old_pos, "right")
    elif old_dir =="right":
        if int(x) == len(rows[0])-1:
            return "end;"
        if rows[int(y)][int(x)+1] in [".", "^"]:
            return f"{int(x)+1},{int(y)};right"
        else:
            return next_pos(rows, old_pos, "down")
    elif old_dir == "down":
        if int(y) == len(rows)-1:
            return "end;"
        if rows[int(y)+1][int(x)] in [".", "^"]:
            return f"{int(x)},{int(y)+1};down"
        else:
            return next_pos(rows, old_pos, "left")
    elif old_dir == "left":
        if int(x) == 0:
            return "end;"
        if rows[int(y)][int(x)-1] in [".", "^"]:
            return f"{int(x)-1},{int(y)};left"
        else:
            return next_pos(rows, old_pos, "up")

def find_guard(rows: list) -> str:
    """ Find the guard and return coords and direction """
    for irow, row in enumerate(rows):
        for icol, col in enumerate(list(row)):
            if col == "^":
                return f"{icol},{irow};up"

def count_positions(data: str) -> int:
    """ Count the number of positions the guard will visit """
    positions = []
    rows = [list(row) for row in data.split("\n")]
    pos, direction = find_guard(rows).split(";")
    while pos != "end":
        positions.append(f"{pos};{direction}")
        location = next_pos(rows, pos, direction)
        pos, direction = location.split(";")
    return len(set(_.split(";")[0] for _ in positions))

assert count_positions(test_data) == 41

print(f"Part 1: {count_positions(input_data)}")

# Part 2
def count_loopable_positions(data: str) -> int:
    """ Count the number of location for an obstruction to cause a loop """
    checked_positions= []
    positions = []
    rows = [list(row) for row in data.split("\n")]
    pos, direction = find_guard(rows).split(";")
    # Follow the original guard root. At each step, put an object infront and see if it causes a loop
    while pos != "end":
        location = next_pos(rows, pos, direction)
        # Put an object in the location and calculate route
        if location == "end;":  # Ignore if reached end of the map!
            break
        obj_x, obj_y = location.split(";")[0].split(",")
        rows_edited = deepcopy(rows)  # Take a copy of the map to add object and test route
        rows_edited[int(obj_y)][int(obj_x)] = "$"  # Add object
        it_positions = []  # Check positions visited in current iteration
        starting_pos = find_guard(rows_edited)  # Will return None if object in starting position
        if starting_pos and location.split(";")[0] not in checked_positions:
            checked_positions.append(location.split(";")[0])
            it_pos, it_direction = starting_pos.split(";")
            while it_pos != "end":
                it_location = next_pos(rows_edited, it_pos, it_direction)
                if it_location in it_positions:  # Check if visited position before in this iteration
                    positions.append(location)  # Add object location to positions which cause a loop
                    break
                it_positions.append(it_location)  # New position so add to iteration positions
                it_pos, it_direction = it_location.split(";")  # Decode next position and direction
        location = next_pos(rows, pos, direction)
        pos, direction = location.split(";")
    return len(set(_.split(";")[0] for _ in positions))

assert count_loopable_positions(test_data) == 6

print(f"Part 2: {count_loopable_positions(input_data)}")