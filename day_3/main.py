""" Day Two of Advent of Code 2023"""
from math import prod


def find_symbols(row, star_only=False) -> list:
    """Find symbols in a row and add to list"""
    symbol_cols = []
    # Find Symbols
    for ncol, col in enumerate([_ for _ in row]):
        if star_only:
            if col == "*":
                symbol_cols.append(ncol)
        else:
            if not col.isdigit() and not col == ".":
                symbol_cols.append(ncol)
    return symbol_cols


# Part 1
def part_1(data) -> int:
    """Return the sum of valid part numbers"""
    rows = data.split("\n")
    symbols = []
    # Find Symbols
    for nrow, row in enumerate(rows):
        for symbol_col in find_symbols(row):
            symbols.append((nrow, symbol_col))

    # Find digits
    skip = 0
    sum_of_part_numbers = 0
    valid = False
    for nrow, row in enumerate(rows):
        for i, char in enumerate(list(row)):
            # Skip if looking at the same number as previous char (i.e the 9 in "109")
            if skip > 0:
                # Check each number in the digit is valid
                skip -= 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        valid = valid or (nrow + dy, i + dx) in symbols
                if skip == 0:
                    # print(valid)
                    if valid:
                        sum_of_part_numbers += int(digit)
                    valid = False
                continue
            # Check if char is a digit and find full number
            if char.isdigit():
                digit = char
                # Check if valid
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        valid = valid or (nrow + dy, i + dx) in symbols
                try:
                    while row[i + 1].isdigit():
                        digit += row[i + 1]
                        i += 1
                        skip += 1
                except IndexError:
                    pass
                # print(digit)
                if not skip:
                    if valid:
                        sum_of_part_numbers += int(digit)
                    # print(valid)
                    valid = False
    return sum_of_part_numbers


def add_gear(gears, digit: int, gear_loc: str):
    # print(f"Digit {digit} touches gear at {gear_loc}")
    gears[gear_loc] += (digit,)
    return gears


def part_2(data) -> int:
    """Part 2 function"""
    rows = data.split("\n")
    symbols = []
    # Find Symbols
    for nrow, row in enumerate(rows):
        for symbol_col in find_symbols(row, star_only=True):
            symbols.append((nrow, symbol_col))
    gears = {str(_): () for _ in symbols}

    # Find digits
    skip = 0
    gear_links = []
    for nrow, row in enumerate(rows):
        if nrow == 9:
            pass
        for i, char in enumerate(list(row)):
            # Skip if looking at the same number as previous char (i.e the 9 in "109")
            if skip > 0:
                # Check each number in the digit is valid
                skip -= 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if str((nrow + dy, i + dx)) in gears.keys():
                            gear_links.append(str((nrow + dy, i + dx)))
                if skip == 0:
                    for link in gear_links:
                        gears = add_gear(gears, int(digit), link)
                        gear_links = []
                continue
            # Check if char is a digit and find full number
            if char.isdigit():
                digit = char
                # Check if valid
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if str((nrow + dy, i + dx)) in gears.keys():
                            gear_links.append(str((nrow + dy, i + dx)))
                try:
                    while row[i + 1].isdigit():
                        digit += row[i + 1]
                        i += 1
                        skip += 1
                except IndexError:
                    pass
                if skip == 0:
                    for link in gear_links:
                        gears = add_gear(gears, int(digit), link)
                        gear_links = []
    total_gear_ratio = sum(
        [prod(set(ratios)) for ratios in gears.values() if len(set(ratios)) >= 2]
    )
    return total_gear_ratio


if __name__ == "__main__":
    import os

    fp = os.path.abspath("") + "\\day_3\\puzzle_input.txt"
    print(fp)
    # Part 1
    with open(fp, "r", encoding="UTF-8") as f:
        schematic = f.read().strip()
        sum_of_parts = part_1(schematic)
        sum_of_gear_ratios = part_2(schematic)

    print(f"Part 1: {sum_of_parts}")
    print(f"Part 2: {sum_of_gear_ratios}")
