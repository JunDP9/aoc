import numpy as np
import sys


# np.set_printoptions(threshold=sys.maxsize)

def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            if str(line) != '':
                coefficients.append(str(line)
                                    .strip()
                                    .replace(',', ' ', 2)
                                    .replace('->', '')
                                    )  # parse them in some way
    return coefficients


def get_largest_x_y_values(input):
    all_x = []
    all_y = []
    for line in input:
        split_line_of_numbers = line.split()
        all_x.append(split_line_of_numbers[0])
        all_x.append(split_line_of_numbers[2])
        all_y.append(split_line_of_numbers[1])
        all_y.append(split_line_of_numbers[3])

    return [max(all_x), max(all_y)]


def initialize_grid(size):
    return np.zeros((size, size)).astype('int')


def count_sum_larger_or_equal_to(grid, value):
    sum = (grid >= 2).sum()
    print(sum)


def draw_line(grid, command):
    # adjust row, same y value
    if command[1] == command[3]:
        list_y_values = [int(command[0]), int(command[2])]
        grid[int(command[1])][min(list_y_values):max(list_y_values) + 1] += 1
    # adjust column, same x value
    if command[0] == command[2]:
        list_y_values = [int(command[1]), int(command[3])]
        grid[:, int(command[0])][min(list_y_values):max(list_y_values) + 1] += 1


def main():
    lines = input_file('input.txt')
    # assume grid is 1000x1000
    # print(get_largest_x_y_values(lines))
    grid = initialize_grid(1000)
    for command in lines:
        # print(command.split())
        draw_line(grid, command.split())
    count_sum_larger_or_equal_to(grid, 2)
    print(grid)


main()
