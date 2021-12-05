import numpy as np


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


def checkDiagonal(x1,y1,x2,y2):
    final_coordinates = [x2, y2]
    for idx in range(0, 1000):
        left_up = [x1-idx, y1-idx]
        left_down = [x1+idx, y1-idx]
        right_up = [x1-idx, y1+idx]
        right_down = [x1+idx, y1+idx]

        if final_coordinates == left_up:
            return 'LEFT_UP'
        if final_coordinates == left_down:
            return 'LEFT_DOWN'
        if final_coordinates == right_up:
            return 'RIGHT_UP'
        if final_coordinates == right_down:
            return 'RIGHT_DOWN'
    return 'NONE'


def draw_line_diagonal(grid, x1, y1, x2, y2, diagonality_command):
    print(diagonality_command)
    final_coordinates = [x2,y2]
    starting_coordinates = [x1,y1]
    for idx in range(0, 1000):
        if diagonality_command == 'LEFT_UP':
            grid[y1-idx][x1-idx] += 1
            starting_coordinates = [x1-idx, y1-idx]
        if diagonality_command == 'LEFT_DOWN':
            grid[y1-idx][x1+idx] += 1
            starting_coordinates = [x1+idx, y1-idx]
        if diagonality_command == 'RIGHT_UP':
            grid[y1+idx][x1-idx] += 1
            starting_coordinates = [x1-idx, y1+idx]
        if diagonality_command == 'RIGHT_DOWN':
            grid[y1+idx][x1+idx] += 1
            starting_coordinates = [x1+idx, y1+idx]
        if starting_coordinates == final_coordinates:
            return


def draw_line(grid, command):
    # adjust row, same y value
    x1 = int(command[0])
    y1 = int(command[1])
    x2 = int(command[2])
    y2 = int(command[3])
    diagonality_command = checkDiagonal(x1, y1, x2, y2)

    if y1 == y2:
        list_x_values = [x1, x2]
        grid[y1][min(list_x_values):max(list_x_values) + 1] += 1

    if x1 == x2:
        list_x_values = [y1, y2]
        grid[:, x1][min(list_x_values):max(list_x_values) + 1] += 1

    if diagonality_command is not 'NONE':
        draw_line_diagonal(grid, x1, y1, x2, y2, diagonality_command)


def main():
    lines = input_file('input.txt')
    grid = initialize_grid(1000)
    for command in lines:
        draw_line(grid, command.split())
    count_sum_larger_or_equal_to(grid, 2)
    print(grid)


main()
