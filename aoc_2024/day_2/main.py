""" Day Two of Advent of Code 2024"""

with open("aoc_2024/day_2/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

reports = []
for line in input_data.split("\n"):
    reports.append(line.split(" "))

# Part 1
def is_safe(vals: list) -> bool:
    """ Check the report values are all rising or decresing by a max increment of 3"""
    diffs = [-(int(vals[i]) - int(vals[i+1])) for i in range(len(vals) - 1)]
    if not all([_ > 0 for _ in diffs]) and not all([_ < 0 for _ in diffs]):
        return False
    if max([max(diffs), abs(min(diffs))]) > 3:
        return False
    return True

assert is_safe([7, 6, 4, 2, 1]) is True
assert is_safe([1, 2, 7, 8, 9]) is False
assert is_safe([9, 7, 6, 2, 1]) is False
assert is_safe([1, 3, 2, 4, 5]) is False
assert is_safe([8, 6, 4, 4, 1]) is False
assert is_safe([1, 3, 6, 7, 9]) is True

safe_reports = sum(is_safe(report) for report in reports)

print(f"Part 1: {safe_reports}")

# Part 2
def problem_dampener(vals: list) -> bool:
    """ Check the report values are all rising or decresing by a max increment of 3 with the 
    allowance of 1 bad number"""
    if is_safe(vals) is True:
        return True
    for i in range(len(vals)):
        vals_original = vals.copy()
        vals_original.pop(i)
        if is_safe(vals_original):
            return True
    return False

assert problem_dampener([7, 6, 4, 2, 1]) is True
assert problem_dampener([1, 2, 7, 8, 9]) is False
assert problem_dampener([9, 7, 6, 2, 1]) is False
assert problem_dampener([1, 3, 2, 4, 5]) is True
assert problem_dampener([8, 6, 4, 4, 1]) is True
assert problem_dampener([1, 3, 6, 7, 9]) is True

safe_reports = sum(problem_dampener(report) for report in reports)

print(f"Part 2: {safe_reports}")
