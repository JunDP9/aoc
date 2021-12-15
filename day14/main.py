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


def compute_v2(my_dict, starting_string, steps):
    start_time = time.time()
    for step in range(0, steps):
        print(step)
        padded_list = ['XXX']*(2*len(starting_string)-1)
        padded_list[::2] = starting_string
        for idx in range(1, len(padded_list), 2):
            char_combo = (padded_list[idx-1] + padded_list[idx+1])
            if char_combo in my_dict:
                padded_list[idx] = my_dict[char_combo]
        starting_string = padded_list

    counter = Counter(starting_string)
    min_key, min_count = min(counter.items(), key=itemgetter(1))
    max_key, max_count = max(counter.items(), key=itemgetter(1))
    print("--- %s seconds ---" % (time.time() - start_time))

    return max_count, max_key, min_count, min_key


def part_two(inputs):
    starting_string = list(inputs[0])
    my_dict = inputs[1]
    max_count, max_key, min_count, min_key = compute_v2(my_dict, starting_string, 40)
    print(min_key, min_count)
    print(max_key, max_count)
    print(max_count - min_count)


def main():
    inputs = input_file('input.txt')
    # part_one(inputs)
    part_two(inputs)


main()
