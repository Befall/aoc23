DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-={}[]/?><\"':;"

# Get all numbers and their row/col coords (ie, in the example, 467 would have [(0,0), (0,1), (0,2)])
def get_number_coords(input_file):
    with open(input_file, "r") as read_file:
        row = -1
        num_coords = []
        is_num = False
        curr_num_set = set()
        curr_num = ''

        for line in read_file:
            if is_num:
                is_num = False
                num_coords.append((curr_num, curr_num_set))
                curr_num_set = set()

            row += 1
            line = line.strip()
            curr_num_set = set()

            for col in range(len(line)):
                if line[col] in DIGITS:
                    if not is_num:
                        is_num = True
                        curr_num = line[col]
                        curr_num_set.add((row, col))
                    else:
                        curr_num += line[col]
                        curr_num_set.add((row, col))
                else:
                    if is_num:
                        is_num = False
                        num_coords.append((curr_num, curr_num_set))
                        curr_num_set = set()
        
    return num_coords

# Get all symbols, check for nearby numbers, and add them to a final list
def get_symbol_coords(input_file):
    with open(input_file, "r") as read_file:
        row = -1
        symbol_coords = []

        for line in read_file:
            row += 1
            line = line.strip()
            for col in range(len(line)):
                if line[col] in SYMBOLS:
                    symbol_coords.append((row, col))

    return symbol_coords

# Get all gear (*) coords
def get_gear_coords(input_file):
    with open(input_file, "r") as read_file:
        row = -1
        gear_coords = []

        for line in read_file:
            row += 1
            line = line.strip()
            for col in range(len(line)):
                if line[col] == "*":
                    gear_coords.append((row, col))

    return gear_coords

INPUT_FILE = "input.txt"

part1 = False
if part1:
    number_coords = get_number_coords(INPUT_FILE)
    symbol_coords = get_symbol_coords(INPUT_FILE)

    total_engine = 0
    added_coords = set()
    for sc in symbol_coords:
        x = sc[0]
        y = sc[1]
        adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]

        for num, coords in number_coords:
            for a in adjacent_coords:
                if a in coords and a not in added_coords:
                    total_engine += int(num)
                    for c in coords:
                        added_coords.add(c)

    print(total_engine)
else:
    number_coords = get_number_coords(INPUT_FILE)
    gear_coords = get_gear_coords(INPUT_FILE)
    total_gear = 0

    for gc in gear_coords:
        x = gc[0]
        y = gc[1]
        adjacent_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]

        adjacent_nums = []
        adjacent_num_coords = set()

        for num, coords in number_coords:
            for a in adjacent_coords:
                if a in coords and a not in adjacent_num_coords:
                    adjacent_nums.append(int(num))
                    for c in coords:
                        adjacent_num_coords.add(c)
        
        if len(adjacent_nums) == 2:
            total_gear += adjacent_nums[0] * adjacent_nums[1]

    print(total_gear)
