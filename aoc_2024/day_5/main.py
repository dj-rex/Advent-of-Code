""" Day Five of Advent of Code 2024"""
from random import shuffle

with open("aoc_2024/day_5/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

with open("aoc_2024/day_5/test_input", encoding="utf-8") as f:
    test_data = f.read().strip()

# Part 1
def parse_input(data: str):
    """ Turn input into lists of rules and updates"""
    codes = data.split("\n")
    rules = [code for code in codes if "|" in code]
    updates = [code for code in codes if "," in code]
    return rules, updates

def check_update(rules: list, update:list) ->int:
    """ Check the update conforms to the rules. Return middle page number if True """
    for rule in rules:
        r1, r2 = rule.split("|")
        if r1 in update and r2 in update:
            if not update.index(r1) < update.index(r2):
                return 0
    return int(update[int(len(update)/2)])

def sum_correct_updates(data: str):
    """ Sum middle page of upates if they conform to rules """
    rules, updates = parse_input(data)
    return sum(check_update(rules, update.split(",")) for update in updates)

assert sum_correct_updates(test_data) == 143

print(f"Part 1: {sum_correct_updates(input_data)}")

# Part 2
def correct_update(rules:list, update:list) -> int:
    """ Apply rules in random order until update is valid """
    while check_update(rules, update) == 0:
        shuffle(rules)
        for rule in rules:
            r1, r2 = rule.split("|")
            if r1 in update and r2 in update:
                while update.index(r1) > update.index(r2):
                    i = update.index(r1)
                    update[i] = update[i-1]
                    update[i-1] = r1
    return check_update(rules, update)

def correct_order_before_sum(data: str):
    """ Correct order and sum middle pages of invalid updates """
    rules, updates = parse_input(data)
    page_nums = []
    for update in updates:
        if check_update(rules, update.split(",")) != 0:
            continue
        page_num = correct_update(rules, update.split(","))
        page_nums.append(page_num)
    return sum(page_nums)

assert correct_order_before_sum(test_data) == 123

print(f"Part 2: {correct_order_before_sum(input_data)}")
