""" Day Four of Advent of Code 2023"""


# Part 1
def part_1(data) -> int:
    """Return the sum of valid scratchcard numbers"""
    total = 0
    for row in data.split("\n"):
        numbers = row.split(": ")[1]
        winners = numbers.split(" | ")[0].split(" ")
        values = numbers.split(" | ")[1].split(" ")
        winning_numbers = set(winners) & set(values)
        try:
            winning_numbers.remove("")
        except:
            pass
        finally:
            if winning_numbers:
                total += 2 ** (len(winning_numbers) - 1)
    return total


def part_2(data) -> int:
    """Part 2 function"""
    total = 0
    rows = data.split("\n")
    for i in range(0, len(rows)):
        print(f"On row {i}")
        total += process_row(rows, i)
    return total


def process_row(rows, nrow) -> int:
    if nrow > len(rows) - 1:
        return 0
    number_of_cards = 1
    row = rows[nrow]
    numbers = row.split(": ")[1]
    winners = numbers.split(" | ")[0].split(" ")
    values = numbers.split(" | ")[1].split(" ")
    winning_numbers = set(winners) & set(values)
    try:
        winning_numbers.remove("")
    except:
        pass
    finally:
        if winning_numbers:
            for i in range(0, len(winning_numbers)):
                number_of_cards += process_row(rows, nrow + i + 1)
    return number_of_cards


if __name__ == "__main__":
    import os

    fp = os.path.abspath("") + "\\day_4\\puzzle_input.txt"
    print(fp)
    # Part 1
    with open(fp, "r", encoding="UTF-8") as f:
        schematic = f.read().strip()
        points = part_1(schematic)
        cards = part_2(schematic)

    print(f"Part 1: {points}")
    print(f"Part 2: {cards}")
