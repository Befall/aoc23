from functools import reduce
import re

INPUT_FILE = "input.txt"

def get_entries(line):
    # Both parts
    return [int(i) for i in re.split(" +", line)[1:]]

def race(time, distance):
    # Both parts
    winners = 0
    for i in range(time + 1):
        remaining = time - i
        speed = remaining * i
        if speed > distance:
            winners += 1
    return winners

def find_winning_times():
    # Part one
    winning_times = []
    with open(INPUT_FILE, "r") as read_file:
        times = get_entries(read_file.readline())
        distances = get_entries(read_file.readline())
        for t, d in zip(times, distances):
            winning_times.append(race(t, d))
    return winning_times

def find_megawinning_time():
    # Part two
    with open(INPUT_FILE, "r") as read_file:
        times = get_entries(read_file.readline())
        distances = get_entries(read_file.readline())
        time = int(''.join(map(str, times)))
        distance = int(''.join(map(str, distances)))
        return race(time, distance)

PART_ONE = False
if PART_ONE:
    print(reduce(lambda x, y: x * y, find_winning_times()))
else:
    print(find_megawinning_time())
