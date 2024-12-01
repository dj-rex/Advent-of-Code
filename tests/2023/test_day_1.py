""" Test Day 1 """
from aoc_2023.day_1 import part_1_parser, part_2_parser


def test_part_1():
    """Test part 1 parser"""
    assert part_1_parser("1abc2") == 12
    assert part_1_parser("pqr3stu8vwx") == 38
    assert part_1_parser("a1b2c3d4e5f") == 15
    assert part_1_parser("treb7uchet") == 77


def test_part_2():
    """Test part 2 parser"""
    assert part_2_parser("two1nine") == 29
    assert part_2_parser("eightwothree") == 83
    assert part_2_parser("abcone2threexyz") == 13
    assert part_2_parser("xtwone3four") == 24
    assert part_2_parser("4nineeightseven2") == 42
    assert part_2_parser("zoneight234") == 14
    assert part_2_parser("7pqrstsixteen") == 76
