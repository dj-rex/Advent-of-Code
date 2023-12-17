""" Day Five of Advent of Code 2023"""


# Part 1
def part_1(data) -> int:
    """Part 1 function"""
    return 0


def part_2(data) -> int:
    """Part 2 function"""
    return 0


if __name__ == "__main__":
    import os

    fp = os.path.abspath("") + "\\day_5\\puzzle_input.txt"

    # Part 1
    with open(fp, "r", encoding="UTF-8") as f:
        schematic = f.read()
        p1 = part_1(schematic)
        p2 = part_2(schematic)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
