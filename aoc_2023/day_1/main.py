""" Day One of Advent of Code 2023"""


# Part 1
def part_1_parser(input_line: str) -> int:
    """Return the first and last integer in the line as a single integer"""
    digits = [int(_) for _ in str(input_line) if _.isdigit()]
    return int(str(digits[0]) + str(digits[-1]))


# Part 2
ints = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_2_parser(input_line: str):
    """Return the first and last integer in the line as a single integer having replaced
    string integers to real integers"""
    # Find first digit
    line_copy = input_line
    first_digit = 0
    while first_digit == 0:
        if line_copy[0].isdigit():
            first_digit = line_copy[0]
        else:
            for int_name, int_val in ints.items():
                if line_copy[: len(int_name)] == int_name:
                    first_digit = int_val
                    break
        line_copy = line_copy[1:]
    # Find last digit
    line_copy = input_line
    last_digit = 0
    while last_digit == 0:
        if (line_copy[-1]).isdigit():
            last_digit = line_copy[-1]
        else:
            for int_name, int_val in ints.items():
                if line_copy[-len(int_name) :] == int_name:
                    last_digit = int_val
                    break
        line_copy = line_copy[:-1]
    return int(str(first_digit) + str(last_digit))


if __name__ == "__main__":
    import os

    fp = os.getcwd() + "\\day_1\\puzzle_input.txt"

    # Part 1
    with open(fp, "r", encoding="UTF-8") as f:
        cal_vals = []
        for line in f:
            cal_vals.append(part_1_parser(line))

    print(f"Part 1: {sum(cal_vals)}")

    # Part 2
    with open(fp, "r", encoding="UTF-8") as f:
        cal_vals = []
        for line in f:
            cal_vals.append(part_2_parser(line))
    print(f"Part 2: {sum(cal_vals)}")
