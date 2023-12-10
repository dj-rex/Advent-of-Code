""" Day Two of Advent of Code 2023"""


# Part 1
def part_1_line_possible(
    input_line: str, max_green: int, max_blue: int, max_red: int
) -> int:
    """Return the ID if game possible"""
    game, result = input_line.split(":")
    game_id = int(game.replace("Game ", ""))
    results = [_.strip() for _ in result.split(";")]
    for result in results:
        draws = result.split(", ")
        for draw in draws:
            balls, colour = draw.split(" ")
            game_id = 0 if colour == "green" and int(balls) > max_green else game_id
            game_id = 0 if colour == "blue" and int(balls) > max_blue else game_id
            game_id = 0 if colour == "red" and int(balls) > max_red else game_id
    return game_id


def part_2(input_line: str) -> int:
    """Return the ID if game possible"""
    game, result = input_line.split(":")
    game_id = int(game.replace("Game ", ""))
    results = [_.strip() for _ in result.split(";")]
    req_green = 0
    req_blue = 0
    req_red = 0
    for result in results:
        draws = result.split(", ")
        for draw in draws:
            balls, colour = draw.split(" ")
            req_green = (
                int(balls)
                if colour == "green" and int(balls) > req_green
                else req_green
            )
            req_blue = (
                int(balls) if colour == "blue" and int(balls) > req_blue else req_blue
            )
            req_red = (
                int(balls) if colour == "red" and int(balls) > req_red else req_red
            )
    return req_green * req_blue * req_red


if __name__ == "__main__":
    import os

    fp = os.getcwd() + "\\day_2\\puzzle_input.txt"

    # Part 1
    with open(fp, "r", encoding="UTF-8") as f:
        id_sum = 0
        power_sum = 0
        for line in f:
            id_sum += part_1_line_possible(line, max_green=13, max_blue=14, max_red=12)
            power_sum += part_2(line)

    print(f"Part 1: {id_sum}")
    print(f"Part 2: {power_sum}")
