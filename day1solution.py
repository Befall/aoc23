import re

total = 0
with open("input.txt", "r") as r:
    for line in r:
        # Sub spelled out digits
        digit_text_to_int = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        # Find all matches, both text and digit
        matches = []
        for s, d in digit_text_to_int.items():
            found = [m.span()[0] for m in re.finditer(s, line)]
            found += [m.span()[0] for m in re.finditer(str(d), line)]
            if found:
                for f in found:
                    matches.append((f, str(d)))

        # Sort them by index found, grab the first/last, and add em
        matches = sorted(matches, key=lambda x: x[0])
        total += int(matches[0][1] + matches[-1][1])

print(total)
