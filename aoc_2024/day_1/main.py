""" Day One of Advent of Code 2024"""
from collections import Counter

with open("aoc_2024/day_1/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

# Test data
test_list_a = [3,4,2,1,3,3]
test_list_b = [4,3,5,3,9,3]

# Convert puzzle input to 2 lists of integers
list_a = []
list_b = []
for line in input_data.split("\n"):
    id1, id2 = line.split(" ", 1)
    list_a.append(int(id1))
    list_b.append(int(id2))

# Part 1
def calc_list_diff(l1, l2) -> int:
    """Calculate the sum of the difference in two lists of numbers when both in ascending order"""
    return sum([abs(val_1 - val_2) for val_1, val_2 in zip (sorted(l1), sorted(l2))])

assert calc_list_diff(test_list_a, test_list_b) == 11

print(f"Part 1: {calc_list_diff(list_a, list_b)}")

#Part 2
def similarity_score(l1, l2) -> int:
    """Calculate the sum of the product of the numbers in the first list by the times they appear in the second list"""
    c = Counter(l2)
    return sum([i*c[i] for i in l1])

assert similarity_score(test_list_a, test_list_b) == 31

print(f"Part 2: {similarity_score(list_a, list_b)}")
