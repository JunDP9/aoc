def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients.append((str(line)
                                 .replace(' |', '').rstrip('\n')
                                 ).split())  # parse them in some way
    return list(coefficients)


def part_one(list):
    amount = [0] * 4
    for line in list:
        first_digit = len(line[10])
        second_digit = len(line[11])
        third_digit = len(line[12])
        fourth_digit = len(line[13])

        if first_digit == 2:
            amount[0] += 1
        if second_digit == 2:
            amount[0] += 1
        if third_digit == 2:
            amount[0] += 1
        if fourth_digit == 2:
            amount[0] += 1

        if first_digit == 3:
            amount[1] += 1
        if second_digit == 3:
            amount[1] += 1
        if third_digit == 3:
            amount[1] += 1
        if fourth_digit == 3:
            amount[1] += 1

        if first_digit == 4:
            amount[2] += 1
        if second_digit == 4:
            amount[2] += 1
        if third_digit == 4:
            amount[2] += 1
        if fourth_digit == 4:
            amount[2] += 1

        if first_digit == 7:
            amount[3] += 1
        if second_digit == 7:
            amount[3] += 1
        if third_digit == 7:
            amount[3] += 1
        if fourth_digit == 7:
            amount[3] += 1


    print(sum(amount))


def get_corresponding_number(digit):
    if len(digit) == 2:
        return 1
    elif len(digit) == 3:
        return 7
    elif len(digit) == 4:
        return 4
    elif len(digit) == 7:
        return 8

def determine_three(zero_six_nine, seven, five_flag):
    for digit in zero_six_nine:
        parse_string = lambda chars, string: [char in string for char in chars]
        check_values = parse_string(digit, seven) if five_flag else parse_string(seven, digit)
        if all(check_values):
            return digit


def part_two(numbers):
    total_amount = 0
    for line in numbers:
        my_dict = {}
        determine_unique_digit_numbers(line, my_dict)

        two_three_five = list(filter(lambda x: len(x) == 5, my_dict))
        zero_six_nine = list(filter(lambda x: len(x) == 6, my_dict))

        seven_four_combined = list(set(list(my_dict.keys())[list(my_dict.values()).index(str(7))] + list(my_dict.keys())[list(my_dict.values()).index(str(4))]))
        nine = determine_three(zero_six_nine, seven_four_combined, False)

        three = determine_three(two_three_five, list(my_dict.keys())[list(my_dict.values()).index(str(7))], False)

        two_five = list(filter(lambda x: x != three, two_three_five))
        zero_six = list(filter(lambda x: x != nine, zero_six_nine))

        five = determine_three(two_five, nine, True)
        two = list(filter(lambda x: x != five, two_five))[0]

        six = determine_three(zero_six, five, False)
        zero = list(filter(lambda x: x != six, zero_six))[0]

        my_dict[nine] = str(9)
        my_dict[three] = str(3)
        my_dict[five] = str(5)
        my_dict[two] = str(2)
        my_dict[zero] = str(0)
        my_dict[six] = str(6)

        final_number = calculate_final_number(line, my_dict)
        total_amount += int(final_number)

    print(total_amount)


def calculate_final_number(line, my_dict):
    final_number = ''
    for idx in range(0, 4):
        final_number += my_dict[''.join(sorted(line[idx + 10]))]
    return final_number


def determine_unique_digit_numbers(line, my_dict):
    for digit in line:
        if ''.join(sorted(digit)) not in my_dict:
            my_dict[''.join(sorted(digit))] = str(get_corresponding_number(digit))


def main():
    list = input_file('input.txt')
    part_one(list)
    part_two(list)


main()
