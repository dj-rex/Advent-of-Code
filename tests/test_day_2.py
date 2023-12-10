""" Test Day 2 """
from day_2 import part_1_line_possible, part_2


def test_part_1_returns_id():
    """Test part 1"""
    line = "Game 1: 3 blue, 4 red, 3 green; 5 blue, 3 red, 2 green"
    assert part_1_line_possible(line, max_green=13, max_blue=14, max_red=12) == 1
    line = "Game 11: 3 blue, 4 red, 3 green; 5 blue, 3 red, 2 green"
    assert part_1_line_possible(line, max_green=13, max_blue=14, max_red=12) == 11


def test_part_1_enforces_limit():
    """Test part 1"""
    line = "Game 1: 30 blue, 4 red, 3 green; 5 blue, 3 red, 2 green"
    assert part_1_line_possible(line, max_green=13, max_blue=14, max_red=12) == 0
    line = "Game 11: 3 blue, 4 red, 3 green; 5 blue, 30 red, 2 green"
    assert part_1_line_possible(line, max_green=13, max_blue=14, max_red=12) == 0


def test_part_2():
    """Test part 2"""
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert part_2(line) == 48
    line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    assert part_2(line) == 12
    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert part_2(line) == 1560
    line = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    assert part_2(line) == 630
    line = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    assert part_2(line) == 36
