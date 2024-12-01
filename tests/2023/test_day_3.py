""" Test Day 3 """
from aoc_2023.day_3 import part_1, part_2

test_str = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."


# Part 1
def test_part_1():
    """Part 1 test"""
    assert part_1(test_str) == 4361


def test_part_2():
    """Part 1 test"""
    assert part_2(test_str) == 467835
