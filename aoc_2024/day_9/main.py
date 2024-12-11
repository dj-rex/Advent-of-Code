""" Day 9 of Advent of Code 2024"""
from itertools import chain
with open("aoc_2024/day_9/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_9/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

# Part 1
def replace_free_space(line: list) -> list:
    new_line = [["."] * int(_) if i % 2 != 0 else [str(int(i/2))] * int(_) for i, _ in enumerate(line)]
    flattened_line = list(chain(*new_line))
    return flattened_line
    
def sort_partition(line: list, whole_file:bool) -> list:
    """ Compact partition filling from righthand side to leftmost disk space """
    if not whole_file:
        for i in range(len(line)):
            if set(line[i:]) == set(["."]):
                break
            if line[i] == ".":
                for j in reversed(range(len(line))):
                    if line[j].isdigit():
                        line[i] = line[j]
                        line[j] = "."
                        break
    else:
        prev_max = len(line)
        for i in reversed(range(len(line))):
            if i > prev_max:
                continue    
            if line[i].isdigit():
                if line[i] == "2":
                    pass
                j = 1
                while len(set(line[i-j+1:i+1])) == 1:
                    prev_max = i - j
                    j+=1
                j -= 1
                for k in range(len(line)):
                    if k > i:
                        break
                    if not line[k:k+j] == ["."]*j:
                        continue
                    line[k:k+j] = line[i-j+1:i+1]
                    for n in range(i+1):
                        if n < i-j+1:
                            continue
                        line[n] = "."
                    break
    return line

def calculate_checksum(data: str, whole_file:bool = False) -> int:
    """ Calculate checksum of input string """
    data = replace_free_space(list(data))
    data = sort_partition(data, whole_file)
    checksum = sum(i*int(v) for i, v in enumerate(data) if v.isdigit())
    return checksum

assert calculate_checksum(test_data) == 1928
    

print(f"Part 1: {calculate_checksum(input_data)}")

# Part 2
assert calculate_checksum(test_data, whole_file=True) == 2858

print(f"Part 2: {calculate_checksum(input_data, whole_file=True)}")
