def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients.append((str(line)
                                 .replace(' |', '').rstrip('\n')
                                 ).split())  # parse them in some way
    return list(coefficients)


def calc_amount(list):
    amount = [0] * 4
    for line in list:
        first_digit = len(line[10])

        second_digit = len(line[11])

        third_digit = len(line[12])

        fourth_digit = len(line[13])
        print(amount)
        print(first_digit, second_digit, third_digit, fourth_digit)
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


        print(amount)
        print('------------')
    print(amount)
    print(sum(amount))


def main():
    list = input_file('input.txt')
    print(list)
    calc_amount(list)


#
# def calc_dict(mydict, mylist):
#     for idx in range(0, len(mylist)):
#         for jdx in range(0, len(mylist)):
#             if 'position ' + str(idx) in mydict:
#                 mydict['position ' + str(idx)].append(abs(mylist[idx] - mylist[jdx]))
#             else:
#                 mydict['position ' + str(idx)] = []
#                 mydict['position ' + str(idx)].append(abs(mylist[idx] - mylist[jdx]))
#
#
# def calc_dict_part_2(mydict, mylist):
#     for idx in range(0, len(mylist)):
#         for jdx in range(0, len(mylist)):
#             n = abs((mylist[jdx] - idx))
#             if 'position ' + str(idx) in mydict:
#                 mydict['position ' + str(idx)].append(((n * n) + n) / 2)
#             else:
#                 mydict['position ' + str(idx)] = []
#                 mydict['position ' + str(idx)].append(((n * n) + n) / 2)


main()
