import re

def get_card_wins(split_line):
    winning = re.split(' +', split_line[2].strip())
    possible = re.split(' +', split_line[4].strip())
    line_matches = 0

    for p in possible:
        if p in winning:
            line_matches += 1

    return line_matches

# Part 1
def get_card_points(input_file):
    total = 0
    with open(input_file, "r") as read_file:
        for line in read_file:
            split_line = re.split(r'(:|\|)', line)
            matches = get_card_wins(split_line)
            total += pow(2, matches - 1) if matches else 0
    return total

# Part 2
def get_total_cards(input_file):
    card_wins = {}
    with open(input_file, "r") as read_file:
        for line in read_file:
            split_line = re.split(r'(:|\|)', line)
            card_number = re.sub(r'\D', '', split_line[0])
            card_wins[card_number] = get_card_wins(split_line)

    card_totals = {k: 1 for k in card_wins.keys()}
    for card_num in range(1, len(card_wins)+1):
        card_num_str = str(card_num)
        wins = card_wins[card_num_str]
        inced = list(card_wins.keys())[int(card_num_str):int(card_num_str)+wins]
        for i in inced:
            card_totals[i] += card_totals[card_num_str]

    return(sum(list(card_totals.values())))

INPUT_FILE = "input.txt"
part1 = False
if part1:
    print(get_card_points(INPUT_FILE))
else:
    print(get_total_cards(INPUT_FILE))
