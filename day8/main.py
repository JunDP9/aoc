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
            print('number 1 length is 2 ' + str(line[10]))
            amount[0] += 1
        if second_digit == 2:
            amount[0] += 1
        if third_digit == 2:
            amount[0] += 1
        if fourth_digit == 2:
            amount[0] += 1

        if first_digit == 3:
            print('number 1 length is 3 ' + str(line[10]))
            amount[1] += 1
        if second_digit == 3:
            amount[1] += 1
        if third_digit == 3:
            amount[1] += 1
        if fourth_digit == 3:
            amount[1] += 1

        if first_digit == 4:
            print('number 1 length is 4 ' + str(line[10]))
            amount[2] += 1
        if second_digit == 4:
            amount[2] += 1
        if third_digit == 4:
            amount[2] += 1
        if fourth_digit == 4:
            amount[2] += 1

        if first_digit == 7:
            print('number 1 length is 7 ' + str(line[10]))
            amount[3] += 1
        if second_digit == 7:
            amount[3] += 1
        if third_digit == 7:
            amount[3] += 1
        if fourth_digit == 7:
            amount[3] += 1

        break

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


def determine_nine(zero_six_nine, seven, four):
    seven_four_combined = list(set(seven + four))
    for digit in zero_six_nine:
        parse_string = lambda chars, string: [char in string for char in chars]
        check_values = parse_string(seven_four_combined, digit)
        if (all(check_values)):
            return digit


def determine_three(zero_six_nine, seven):
    for digit in zero_six_nine:
        parse_string = lambda chars, string: [char in string for char in chars]
        check_values = parse_string(list(seven), digit)
        if (all(check_values)):
            return digit


def determine_five(two_five, nine):
    for digit in two_five:
        parse_string = lambda chars, string: [char in string for char in chars]
        check_values = parse_string(list(digit), (nine))
        if (all(check_values)):
            return digit

def determine_six(zero_six, five):
    for digit in zero_six:
        parse_string = lambda chars, string: [char in string for char in chars]
        check_values = parse_string(list(five), digit)
        if (all(check_values)):
            return digit


def part_two(numbers):
    final_amount = 0
    for line in numbers:
        my_dict = {}
        for digit in line:
            if ''.join(sorted(digit)) not in my_dict:
                my_dict[''.join(sorted(digit))] = str(get_corresponding_number(digit))

        two_three_five = list(filter(lambda x: len(x) == 5, my_dict))
        zero_six_nine = list(filter(lambda x: len(x) == 6, my_dict))

        nine = determine_nine(zero_six_nine, list(my_dict.keys())[list(my_dict.values()).index(str(7))],
                              list(my_dict.keys())[list(my_dict.values()).index(str(4))])

        three = determine_three(two_three_five, list(my_dict.keys())[list(my_dict.values()).index(str(7))])

        two_five = list(filter(lambda x: x != three, two_three_five))
        zero_six = list(filter(lambda x: x != nine, zero_six_nine))

        five = determine_five(two_five, nine)
        two = list(filter(lambda x : x != five, two_five))[0]

        six = determine_six(zero_six, five)
        zero = list(filter(lambda x : x != six, zero_six))[0]


        my_dict[nine] = str(9)
        my_dict[three] = str(3)
        my_dict[five] = str(5)
        my_dict[two] = str(2)
        my_dict[zero] = str(0)
        my_dict[six] = str(6)

        final_number = ''
        for idx in range(0, 4):
            final_number += my_dict[ ''.join(sorted(line[idx+10]))]
        final_amount += int(final_number)
        print(final_number)

    print(final_amount)

def main():
    list = input_file('input1.txt')
    part_two(list)


main()
