import numpy as np


def input_file(filename):
    commands = []
    y_vals = []
    x_vals = []
    coordinates = []

    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            stripped_line = str(line).strip()
            stringified_line = stripped_line.split(',')
            command = (stripped_line.split()[2]) if 'fold along ' in stripped_line else ''
            if len(stringified_line) == 2:
                # kolom
                y_vals.append(int(stringified_line[0]))
                # rij
                x_vals.append(int(stringified_line[1]))
                coordinates.append((int(stringified_line[1]), int(stringified_line[0])))
            if len(command) > 0:
                commands.append(command)

    grid = initialize_grid(max(x_vals) +2, max(y_vals) + 1)
    for dot in coordinates:
        grid[dot[0],dot[1]] = 1

    print(grid.shape)

    return [grid, commands]


def initialize_grid(x, y):
    return np.zeros((x, y)).astype('int')


def fold_up(row_number, grid):
    first_half = grid[:row_number, :]
    second_half = grid[row_number + 1:, :]
    inverted_second_half = second_half[::-1]
    resulting_halve = first_half+inverted_second_half
    # print(len(np.nonzero(resulting_halve)[0]))
    return resulting_halve


def fold_left(column_number, grid):
    first_half = grid[:, :column_number]
    second_half = grid[:, column_number + 1:]
    inverted_second_half = second_half[:, ::-1]
    resulting_halve = first_half+inverted_second_half
    # print(len(np.nonzero(resulting_halve)[0]))
    return resulting_halve



def part_one(commands, grid):

    for command in commands:
        split_command = command.split('=')
        if split_command[0] == 'x':
            grid = fold_left(int(split_command[1]), grid)
            # print(grid)
        elif split_command[0] == 'y':
            grid = fold_up(int(split_command[1]), grid)
            # print(grid)
    return grid


def part_two(my_list):
    pass




def main():
    input = input_file('input.txt')
    grid = input[0]
    commands = input[1]
    grid = part_one(commands, grid)
    print(grid)
    # copy pasted code
    s = [[str('#' if e > 0 else '.') for e in row] for row in grid]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
#    EAHKRECP


main()

# list add 1 to all
# for each octopus:
#   if greater than 9:
#     add 1 to all neighbors if not 0
#     turn 0
