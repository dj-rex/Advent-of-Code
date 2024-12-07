""" Day Seven of Advent of Code 2024"""
from itertools import product
with open("aoc_2024/day_7/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_7/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

# Part 1
def solve_equation(vals:list, result:int, inc_bar:bool = False) -> int:
    """ Return the result of the equation if it is a valid equation"""
    if len(vals) == 1:
        return int(result) if vals[0] == int(result) else 0
    op_lists = product("+*|", repeat=len(vals)-1) if inc_bar else product("+*", repeat=len(vals)-1)
    for op_list in list(op_lists):
        total = 0
        for i in range(len(vals)-1):
            total = vals[i] if i == 0 else total
            if op_list[i] == "*":
                total *= vals[i+1]
            elif op_list[i] == "+":
                total += vals[i+1]
            if inc_bar:
                if op_list[i] == "|":
                    total = int(str(total)+str(vals[i+1]))
        if total == int(result):
            return total
    return 0

def sum_of_solutions(data: str) -> int:
    """ Calculate the sum of the solutions to the equations """
    solution_count = 0
    for equation in list(data.split("\n")):
        res, val_str = equation.split(":")
        vals = [int(_) for _ in val_str.strip().split(" ")]
        solution_count += solve_equation(vals, res)
    return solution_count

assert sum_of_solutions(test_data) == 3749

print(f"Part 1: {sum_of_solutions(input_data)}")

# Part 2
def sum_of_solutions_with_new_operand(data: str) -> int:
    """ Calculate the sum of the solutions to the equations including a bar operator """
    solution_count = 0
    for i, equation in enumerate(list(data.split("\n"))):
        res, val_str = equation.split(":")
        vals = [int(_) for _ in val_str.strip().split(" ")]
        solution_count += solve_equation(vals, res, True)
    return solution_count

assert sum_of_solutions_with_new_operand(test_data) == 11387

print(f"Part 2: {sum_of_solutions_with_new_operand(input_data)}")
