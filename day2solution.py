import re
from functools import reduce
from operator import mul

RED = "red"
GREEN = "green"
BLUE = "blue"

NUM_CUBES_POSSIBLE = {
    RED: 12,
    GREEN: 13,
    BLUE: 14,
}

# Part 1
def check_line(line):
    split_line = [i for i in re.split("(:|;)", line) if i not in [';', ':']]
    game_id = re.sub(r'\D', '', split_line[0])

    for c in split_line[1:]:
        cubes = c.split(',')
        for cube in cubes:
            num, color = cube.strip().split(' ')
            if NUM_CUBES_POSSIBLE[color] < int(num):
                return False
    return game_id

# Part 2
def min_possible(line):
    split_line = [i for i in re.split("(:|;)", line) if i not in [';', ':']]
    min_of_each = {
        RED: 0,
        GREEN: 0,
        BLUE: 0,
    }

    for c in split_line[1:]:
        cubes = c.split(',')
        for cube in cubes:
            num, color = cube.strip().split(' ')
            if min_of_each[color] < int(num):
                min_of_each[color] = int(num)

    return reduce(mul, list(min_of_each.values()))

with open("input.txt", "r") as r:
    part1 = False
    total = 0

    if (part1):
        for line in r:
            line_result = check_line(line)
            if line_result:
                total += int(line_result)
    else:
        for line in r:
            total += min_possible(line)
    
    print(total)
