import math
from collections import Counter
from operator import itemgetter
import time


def input_file(filename):
    start_string = ''
    my_dict = {}

    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            stripped_line = str(line).strip()
            if '->' not in stripped_line:
                start_string += stripped_line
            else:
                dict_key_value = stripped_line.split('->')
                my_dict[dict_key_value[0].strip()] = dict_key_value[1].strip()

    return [start_string, my_dict]


def part_one(inputs):
    starting_string = list(inputs[0])
    my_dict = inputs[1]
    compute_v1(my_dict, starting_string, 10)


def compute_v1(my_dict, starting_string, steps):
    start_time = time.time()
    for step in range(0, steps):
        add_counter = 0
        for idx in range(1, len(starting_string)):
            char_combo = (starting_string[idx - 1 + add_counter] + starting_string[idx + add_counter])
            if char_combo in my_dict:
                starting_string.insert(idx + add_counter, my_dict[char_combo])
                add_counter += 1

    print_max_substracted_by_min(starting_string)
    print("--- %s seconds ---" % (time.time() - start_time))


def print_max_substracted_by_min(starting_string):
    counter = Counter(starting_string)
    min_key, min_count = min(counter.items(), key=itemgetter(1))
    max_key, max_count = max(counter.items(), key=itemgetter(1))
    print(min_key, min_count)
    print(max_key, max_count)
    print(max_count - min_count)


def compute_v2(char_amount_dict, combo_to_single_char_dict, empty_exponential_total_dict, exponential_total_dict,
               combo_to_offspring_dict, steps):
    start_time = time.time()
    for step in range(0, steps):
        empty_total_dict = empty_exponential_total_dict.copy()
        for key, value in exponential_total_dict.items():
            empty_total_dict[combo_to_offspring_dict[key][0]] += value
            empty_total_dict[combo_to_offspring_dict[key][1]] += value
            char_amount_dict[combo_to_single_char_dict[key]] += value

        exponential_total_dict = empty_total_dict

    print_max_substracted_by_min(char_amount_dict)
    print("--- %s seconds ---" % (time.time() - start_time))


def make_char_dict(total_dict, starting_string):
    char_dict = {}
    for key, value in total_dict.items():
        split_char_one = list(key)[0]
        split_char_two = list(key)[1]
        if split_char_one not in char_dict:
            char_dict[split_char_one] = 0
        if split_char_two not in char_dict:
            char_dict[split_char_two] = 0
        if value not in char_dict:
            char_dict[value] = 0

    for char in starting_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            print('not in total dict yet')

    return char_dict


def make_comp(my_dict):
    comp_dict = {}
    total_dict = {}
    for key, value in my_dict.items():
        char_combo = list(key)
        char_combo_child_one = char_combo[0] + value
        char_combo_child_two = value + char_combo[1]
        comp_dict[key] = (char_combo_child_one, char_combo_child_two)
        if key not in total_dict:
            total_dict[key] = 0
        if char_combo_child_one not in total_dict:
            total_dict[char_combo_child_one] = 0
        if char_combo_child_two not in total_dict:
            total_dict[char_combo_child_two] = 0
    return [comp_dict, total_dict]


def part_two(inputs):
    starting_string = list(inputs[0])
    combo_to_char_dict = inputs[1]
    extra_dicts = make_comp(combo_to_char_dict)
    comp_dict = extra_dicts[0]
    total_dict = extra_dicts[1]
    char_dict = make_char_dict(combo_to_char_dict, starting_string)
    inter_total_dict = total_dict.copy()
    for idx in range(1, len(starting_string)):
        char_combo = (starting_string[idx - 1] + starting_string[idx])
        if char_combo in total_dict:
            total_dict[char_combo] += 1

    compute_v2(char_dict, combo_to_char_dict, inter_total_dict, total_dict, comp_dict, 40)


def main():
    inputs = input_file('input.txt')
    # part_one(inputs)
    part_two(inputs)
    # 3605805746074
    # 3816397135460


main()
