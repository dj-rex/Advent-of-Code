""" Day 11 of Advent of Code 2024"""
import time
with open("aoc_2024/day_11/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_11/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

def calculate_stones(data: str, blinks: int) -> int:
    """ Calculate number of trailheads from each start location """
    stones = [int(_) for _ in data.split(" ")]
    et = time.time()
    while blinks > 0:
        st = time.time()
        print(f"Blinks remaining: {blinks}. Previous blink time: {int((st-et)/60)} mins {int(int(st-et)%60)} seconds")
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
                new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
            else:
                new_stones.append(stone*2024)
        stones = new_stones
        blinks -= 1
        et = st
    return len(new_stones)

# Part 1
assert calculate_stones(test_data, blinks = 6) == 22
assert calculate_stones(test_data, blinks = 25) == 55312

print(f"Part 1: {calculate_stones(input_data, blinks = 25)}")

# Part 2
print(f"Part 2: {calculate_stones(input_data, blinks = 75)}")
