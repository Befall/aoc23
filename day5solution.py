INPUT_FILE = "input.txt"

def get_raw_maps():
    # Both parts, terrible long function to parse input
    maps = {}
    names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    with open(INPUT_FILE, "r") as read_file:
        reading_numbers = False
        curr_list = []
        curr_name = ""
        for line in read_file:
            if "seeds" in line:
                maps["seeds"] = [int(i) for i in line.strip().split(" ")[1:]]
                continue

            if not line.strip():
                if reading_numbers:
                    reading_numbers = False
                    maps[curr_name] = curr_list
                curr_list = []
                curr_name = ""
                continue

            if not reading_numbers:
                for name in names:
                    if name in line:
                        curr_name = name.replace("-", "_")
                        reading_numbers = True
                continue

            if reading_numbers:
                curr_list.append([int(i) for i in line.strip().split(" ")])

        maps[curr_name] = curr_list

    return maps

def get_map_value(left, raw_map):
    # Part 1
    right = None
    for l in raw_map:
        min_l = l[1]
        max_l = l[1] + l[2]
        if left >= min_l and left <= max_l:
            right = (left - min_l) + l[0]
            break
    return right if right else left

def get_seed_ranges(seeds):
    # Part 2
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    return seed_ranges

def get_map_range(source_range, map_ranges):
    # Part 2
    remaining = [source_range]
    transposed = []
    while remaining:
        restart = False
        for i in range(len(remaining)):
            if restart:
                restart = False
                break
            rem = remaining[i]
            for map_range, diff in map_ranges.items():
                l = map_range[0]
                r = map_range[1]

                l_in = rem[0] >= l and rem[0] <= r
                r_in = rem[1] >= l and rem[1] <= r

                if not l_in and not r_in:
                    continue

                if l_in and r_in:
                    transposed.append((rem[0] + diff, rem[1] + diff))
                    del remaining[i]
                    restart = True
                    break

                if l_in and not r_in:
                    transposed.append((rem[0] + diff, r + diff))
                    del remaining[i]
                    remaining.append((r + 1, rem[1]))
                    restart = True
                    break

                if r_in and not l_in:
                    transposed.append((l + diff, rem[1] + diff))
                    del remaining[i]
                    remaining.append((rem[0], l - 1))
                    restart = True
                    break

            if not restart:
                transposed.append(rem)
                del remaining[i]

    return transposed

def get_map_ranges(raw_map, source_ranges):
    # Part 2
    map_ranges = {}
    for destination, source, rng in raw_map:
        map_ranges[(source, source + rng - 1)] = destination - source

    destination_ranges = []
    for source_range in source_ranges:
        destination_ranges += get_map_range(source_range, map_ranges)

    return destination_ranges

PART_ONE = False

if PART_ONE:
    locations = set()
    raw_maps = get_raw_maps()
    for seed in raw_maps["seeds"]:
        soil = get_map_value(seed, raw_maps["seed_to_soil"])
        fertilizer = get_map_value(soil, raw_maps["soil_to_fertilizer"])
        water = get_map_value(fertilizer, raw_maps["fertilizer_to_water"])
        light = get_map_value(water, raw_maps["water_to_light"])
        temperature = get_map_value(light, raw_maps["light_to_temperature"])
        humidity = get_map_value(temperature, raw_maps["temperature_to_humidity"])
        location = get_map_value(humidity, raw_maps["humidity_to_location"])
        locations.add(location)

    print(min(locations))

else:
    locations = set()
    raw_maps = get_raw_maps()
    seed_ranges = get_seed_ranges(raw_maps["seeds"])
    soil_ranges = get_map_ranges(raw_maps["seed_to_soil"], seed_ranges)
    fertilizer_ranges = get_map_ranges(raw_maps["soil_to_fertilizer"], soil_ranges)
    water_ranges = get_map_ranges(raw_maps["fertilizer_to_water"], fertilizer_ranges)
    light_ranges = get_map_ranges(raw_maps["water_to_light"], water_ranges)
    temperature_ranges = get_map_ranges(raw_maps["light_to_temperature"], light_ranges)
    humidity_ranges = get_map_ranges(raw_maps["temperature_to_humidity"], temperature_ranges)
    location_ranges = get_map_ranges(raw_maps["humidity_to_location"], humidity_ranges)

    print(min([l[0] for l in location_ranges]))
