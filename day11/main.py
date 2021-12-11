def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients.append(list(map(int, list(str(line).strip()))))  # parse them in some way
    return list(coefficients)


def check_octopi(my_list, size_counter):
    print(my_list)

    for idx in range(0, len(my_list)):
        for jdx in range(0, len(my_list[idx])):
            if my_list[idx][jdx] > 9:
                flash((idx, jdx), my_list, size_counter)

    # print(size_counter)


def part_one(my_list):
    step = 100
    size_counter = [0]
    for idx in range(0, step):
        my_list = [[octopus + 1 for octopus in row] for row in my_list]
        check_octopi(my_list, size_counter)
    print(size_counter)


def part_two(my_list):
    step = 0
    size_counter = [0]
    flag_all_not_0 = True
    while flag_all_not_0:
        step += 1
        my_list = [[octopus + 1 for octopus in row] for row in my_list]
        check_octopi(my_list, size_counter)

        if sum(sum(rows) for rows in my_list) == 0:
            flag_all_not_0 = False

    print(step)


def get_neighbors(idx, jdx, my_list):
    positions = [[-1, (0, 0)], [-1, (0, 0)], [-1, (0, 0)], [-1, (0, 0)], [-1, (0, 0)], [-1, (0, 0)], [-1, (0, 0)],
                 [-1, (0, 0)]]
    if 0 < jdx:  # left
        positions[0][0] = (my_list[idx][jdx - 1])
        positions[0][1] = (idx, jdx - 1)
    if 0 < jdx and 0 < idx:  # top left
        positions[1][0] = (my_list[idx - 1][jdx - 1])
        positions[1][1] = (idx - 1, jdx - 1)
    if 0 < idx:  # top
        positions[2][0] = (my_list[idx - 1][jdx])
        positions[2][1] = (idx - 1, jdx)
    if jdx + 1 < len(my_list[idx]) and 0 < idx:  # top right
        positions[3][0] = (my_list[idx - 1][jdx + 1])
        positions[3][1] = (idx - 1, jdx + 1)
    if jdx + 1 < len(my_list[idx]):  # right
        positions[4][0] = (my_list[idx][jdx + 1])
        positions[4][1] = (idx, jdx + 1)
    if jdx + 1 < len(my_list[idx]) and idx + 1 < len(my_list):  # down right
        positions[5][0] = (my_list[idx + 1][jdx + 1])
        positions[5][1] = (idx + 1, jdx + 1)
    if idx + 1 < len(my_list):  # down
        positions[6][0] = (my_list[idx + 1][jdx])
        positions[6][1] = (idx + 1, jdx)
    if 0 < jdx and idx + 1 < len(my_list):  # down left
        positions[7][0] = (my_list[idx + 1][jdx - 1])
        positions[7][1] = (idx + 1, jdx - 1)
    return positions


def flash(location, my_list, size_counter):
    if my_list[location[0]][location[1]] > 9:
        my_list[location[0]][location[1]] = 0
        size_counter[0] = (size_counter[0] + 1)

        # left right top down
        neighbors = get_neighbors(location[0], location[1], my_list)
        for neighbor in neighbors:
            if neighbor[0] > 0:
                my_list[neighbor[1][0]][neighbor[1][1]] += 1
        for neighbor in neighbors:
            if my_list[neighbor[1][0]][neighbor[1][1]] > 9:
                flash(neighbor[1], my_list, size_counter)


def main():
    my_list = input_file('input.txt')
    print(my_list)
    part_one(my_list)
    part_two(my_list)


main()

# list add 1 to all
# for each octopus:
#   if greater than 9:
#     add 1 to all neighbors if not 0
#     turn 0
