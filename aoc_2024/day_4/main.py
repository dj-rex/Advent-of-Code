""" Day Four of Advent of Code 2024"""

with open("aoc_2024/day_4/puzzle_input", encoding="utf-8") as f:
    input_data = f.read().strip()

# Part 1 (Disgusting code - I know)
def gen_diagonals1(rs:list) -> list:
    " Get the diagonals from a list of strings"
    ds = []
    x_lim = len(rs[0])
    y_lim = len(rs)
    len_lim = max([x_lim, y_lim])
    for y in range(y_lim):
        d = rs[y][0]
        x=0
        while y > 0:
            x += 1
            if x >= len_lim:
                continue
            y -= 1
            d += rs[y][x]
        ds.append(d)
    for x in range(x_lim):
        y = y_lim - 1
        if x == 0:
            continue
        d = rs[y][x]
        while x < x_lim - 1:
            x += 1
            y -= 1
            d += rs[y][x]
        ds.append(d)
    return ds

def gen_diagonals2(rs:list) -> list:
    """ Get the other diagonals from a list of strings"""
    ds = []
    x_lim = len(rs[0])
    y_lim = len(rs)
    for y in range(y_lim):
        d = rs[y][x_lim - 1]
        x=x_lim - 1
        while y > 0:
            x -= 1
            if x < 0:
                continue
            y -= 1
            d += rs[y][x]
        ds.append(d[::-1])
    for x in reversed(range(x_lim)):
        y = y_lim - 1
        if x == x_lim - 1:
            continue
        d = rs[y][x]
        while x > 0:
            x -= 1
            y -= 1
            d += rs[y][x]
        ds.append(d[::-1])
    return ds

def xmas_hunter(data: str) -> int:
    """ Find all the XMAS's in a list of strings - like a wordsearch"""
    rows = data.split("\n")
    cols = ["".join([row[i] for row in rows]) for i in range(len(rows))]
    diag1 = gen_diagonals1(rows)
    diag2 = gen_diagonals2(rows)
    total = 0
    total += sum(_.count("XMAS") + _.count("SAMX") for _ in rows)
    total += sum(_.count("XMAS") + _.count("SAMX") for _ in cols)
    total += sum(_.count("XMAS") + _.count("SAMX") for _ in diag1)
    total += sum(_.count("XMAS") + _.count("SAMX") for _ in diag2)
    return total

assert xmas_hunter("MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX") == 18

print(f"Part 1: {xmas_hunter(input_data)}")

# Part 2
def mas_hunter(data: str) -> int:
    """ Find all the MAS X's in the input """
    rows = data.split("\n")
    total = 0
    for i in range(len(rows) - 2):
        for j in range(len(rows[0]) - 2):
            if rows[i+1][j+1] == "A":
                if (rows[i][j] == "M" and rows[i+2][j+2] == "S") or (rows[i][j] == "S" and rows[i+2][j+2] == "M"):
                    if (rows[i+2][j] == "M" and rows[i][j+2] == "S") or (rows[i+2][j] == "S" and rows[i][j+2] == "M"):
                        total += 1
    return total

assert mas_hunter("MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX") == 9

print(f"Part 2: {mas_hunter(input_data)}")
