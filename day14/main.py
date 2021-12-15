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
    max_count, max_key, min_count, min_key = compute_v1(my_dict, starting_string, 10)
    print(min_key, min_count)
    print(max_key, max_count)
    print(max_count - min_count)


def compute_v1(my_dict, starting_string, steps):
    start_time = time.time()
    for step in range(0, steps):
        add_counter = 0
        for idx in range(1, len(starting_string)):
            char_combo = (starting_string[idx - 1 + add_counter] + starting_string[idx + add_counter])
            if char_combo in my_dict:
                starting_string.insert(idx + add_counter, my_dict[char_combo])
                add_counter += 1

    counter = Counter(starting_string)
    min_key, min_count = min(counter.items(), key=itemgetter(1))
    max_key, max_count = max(counter.items(), key=itemgetter(1))
    print("--- %s seconds ---" % (time.time() - start_time))
    return max_count, max_key, min_count, min_key


def compute_v2(inter_total_dict, total_dict, comp_dict, steps):
    start_time = time.time()
    # print(comp_dict)
    for step in range(0, steps):
        empty_total_dict = inter_total_dict.copy()
        for key,value in total_dict.items():
            empty_total_dict[comp_dict[key][0]] += value
            empty_total_dict[comp_dict[key][1]] += value
            # inter_total_dict[key] = 0
        total_dict = (empty_total_dict)

    # print(total_dict)
    final_dict = make_char_dict(total_dict)
    # print(final_dict)

    counter = Counter(final_dict)
    min_key, min_count = min(counter.items(), key=itemgetter(1))
    max_key, max_count = max(counter.items(), key=itemgetter(1))
    print("--- %s seconds ---" % (time.time() - start_time))

    return max_count/2, max_key, min_count/2, min_key


def make_char_dict(total_dict):
    final_dict = {}
    for key, value in total_dict.items():
        split_char_one = list(key)[0]
        split_char_two = list(key)[1]
        if split_char_one in final_dict:
            final_dict[split_char_one] += value
        if split_char_two in final_dict:
            final_dict[split_char_two] += value
        if split_char_one not in final_dict:
            final_dict[split_char_one] = value
        if split_char_two not in final_dict:
            final_dict[split_char_two] = value
    return final_dict


def make_comp(my_dict):
    comp_dict={}
    total_dict={}
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
    my_dict = inputs[1]
    extra_dicts = make_comp(my_dict)
    comp_dict = extra_dicts[0]
    total_dict = extra_dicts[1]

    inter_total_dict = total_dict.copy()
    for idx in range(1, len(starting_string)):
        char_combo = (starting_string[idx - 1] + starting_string[idx])
        if char_combo in total_dict:
            total_dict[char_combo] = 1
    char_dict = make_char_dict(total_dict)
    # print(char_dict)
    max_count, max_key, min_count, min_key =  compute_v2(inter_total_dict, total_dict, comp_dict, 40)
    print(min_key, min_count)
    print(max_key, max_count)
    print(math.ceil((max_count - min_count)))


def main():
    inputs = input_file('input2.txt')
    # part_one(inputs)
    part_two(inputs)


main()
