""" Test Day 4 """
from aoc_2023.day_4 import part_1, part_2

test_str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"


# Part 1
def test_part_1():
    """Part 1 test"""
    assert part_1(test_str) == 13


def test_part_2():
    """Part 1 test"""
    assert part_2(test_str) == 30
