""" Day 11 of Advent of Code 2024"""
from multiprocessing import Pool
from functools import partial
from collections import defaultdict
from copy import deepcopy

with open("aoc_2024/day_11/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_11/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

def calc_stone(val: int, blinks: int) -> int:
    """ Calculate the number of stones resulting from a single starting stone """
    stones = defaultdict(int)
    stones[val] += 1
    while blinks > 0:
        print(f"Blinks remaining: {blinks}.")
        cstones = deepcopy(stones)
        for stone, count in cstones.items():
            if count == 0:
                continue
            str_stone = str(stone)
            if stone == 0:
                stones[1] += 1 * count
                stones[0] -= 1 * count
            elif len(str_stone) % 2 == 0:
                stones[int(str_stone[:len(str_stone)//2])] += 1 * count
                stones[int(str_stone[len(str_stone)//2:])] += 1 * count
                stones[stone] -= 1 * count
            else:
                stones[stone*2024] += 1 * count
                stones[stone] -= 1 * count
        del cstones
        blinks -= 1
    return sum(stones.values())

def calculate_stones(data: str, blinks: int) -> int:
    """ Calculate number of stones after blinking. Create a process for each starting stone"""
    starting_stones = map(int, data.split(" "))
    starting_stones = list(starting_stones)
    with Pool(len(starting_stones)) as p:
        stones = sum(p.map(partial(calc_stone, blinks=blinks), starting_stones))
    return stones

if __name__ == '__main__':
    # Part 1
    assert calculate_stones(test_data, blinks = 6) == 22
    assert calculate_stones(test_data, blinks = 25) == 55312

    print(f"Part 1: {calculate_stones(input_data, blinks = 25)}")

    # # Part 2
    print(f"Part 2: {calculate_stones(input_data, blinks = 75)}")
