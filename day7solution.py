from enum import Enum

INPUT_FILE = "input.txt"
CARDS_RANK = {
    "J": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}
class HandTypes(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

def split_hand_string(sorted_hand):
    # Both parts
    hand_list = []
    curr_char = sorted_hand[0]
    char_len = 1
    for i in range(1, 5):
        if sorted_hand[i] == curr_char:
            char_len += 1
            continue
        hand_list.append(curr_char * char_len)
        curr_char = sorted_hand[i]
        char_len = 1
    hand_list.append(curr_char * char_len)
    return hand_list

def sub_jokers(hand):
    # Part 2
    if "J" not in hand or hand == "JJJJJ":
        return hand

    totals = {}
    for c in hand:
        if c == "J":
            continue
        if c in totals:
            totals[c] += 1
            continue
        totals[c] = 1
    tied_for_highest = [k for k, v in totals.items() if v == totals[sorted(totals.items(), key=lambda x: x[1], reverse=True)[0][0]]]
    if len(tied_for_highest) == 1:
        return hand.replace("J", tied_for_highest[0])
    return hand.replace("J", max(tied_for_highest, key=lambda card: CARDS_RANK[card]))

def get_hand_type(hand, joker):
    # Both parts
    sorted_hand = "".join(sorted(hand))
    sorted_hand = sub_jokers(sorted_hand)
    sorted_hand = "".join(sorted(sorted_hand))
    split_hand = sorted(split_hand_string(sorted_hand), key=len, reverse=True)

    if len(split_hand) == 1:
        return HandTypes.FIVE_KIND
    if len(split_hand) == 2:
        if len(split_hand[0]) == 4:
            return HandTypes.FOUR_KIND
        return HandTypes.FULL_HOUSE
    if len(split_hand) == 3:
        if len(split_hand[0]) == 3:
            return HandTypes.THREE_KIND
        return HandTypes.TWO_PAIR
    if len(split_hand) == 4:
        return HandTypes.ONE_PAIR
    return HandTypes.HIGH_CARD

def get_winnings(joker=False):
    # Both parts
    rankings = []
    with open(INPUT_FILE, "r") as read_file:
        for line in read_file:
            hand, bid = line.split(" ")
            bid = int(bid)
            hand_type = get_hand_type(hand, joker)
            rankings.append((
                hand_type.value,
                CARDS_RANK[hand[0]],
                CARDS_RANK[hand[1]],
                CARDS_RANK[hand[2]],
                CARDS_RANK[hand[3]],
                CARDS_RANK[hand[4]],
                bid
            ))
    rankings = sorted(rankings, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
    return sum([x[6] * (i + 1) for i, x in enumerate(rankings)])

PART_ONE = True
if PART_ONE:
    print(get_winnings())
else:
    print(get_winnings(joker=True))
