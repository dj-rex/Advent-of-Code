""" Day Three of Advent of Code 2024"""

with open("aoc_2024/day_3/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

# Part 1
def decorrupt(data: str) -> bool:
    """ Return sum of product of value pairs in format mul(X, X) hidden in string"""
    potential_muls = data.split("mul(")
    potential_muls = [_.split(")")[0] for _ in potential_muls]
    potential_muls = [_.split(",") for _ in potential_muls if "," in _ and _.count(",") == 1]
    vals = [[int(a),int(b)] for a,b in potential_muls if a.isdigit() and b.isdigit()]
    total = sum(a*b for a, b in vals if a < 1000 and b < 1000)
    return total

assert decorrupt("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

print(f"Part 1: {decorrupt(input_data)}")

# Part 2
def do_instructions(data: str) -> bool:
    """ Decorrupt data after a do() command, ignoring data after a don't() command """
    chunks = [chunk for i, chunk in enumerate(data.split("don't()")) if ("do()" in chunk) or i == 0]
    valid_chunks = [chunk.split("do()",1)[1] if i > 0 else chunk for i, chunk in enumerate(chunks)]
    total = sum(decorrupt(str(chunk)) for chunk in valid_chunks)
    return total

assert do_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48

print(f"Part 2: {do_instructions(input_data)}")
