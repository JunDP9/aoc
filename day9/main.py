def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients.append(list(str(line).strip()))  # parse them in some way
    return list(coefficients)


def part_one(my_list):
    sum = 0
    lowest_positions = []
    for idx in range(0, len(my_list)):
        for jdx in range(0, len(my_list[idx])):
            # left right top down
            neighbors = get_neighbors(idx, jdx, my_list)
            if int(my_list[idx][jdx]) < neighbors[0] and int(my_list[idx][jdx]) < neighbors[1] and int(
                    my_list[idx][jdx]) < neighbors[2] and int(my_list[idx][jdx]) < neighbors[3]:
                sum += (int(my_list[idx][jdx]) + 1)
                lowest_positions.append((idx, jdx))
    print(sum)
    return lowest_positions


def get_neighbors(idx, jdx, my_list):
    positions = [9] * 4
    if 0 < jdx:
        positions[0] = int(my_list[idx][jdx - 1])
    if jdx + 1 < len(my_list[idx]):
        positions[1] = int(my_list[idx][jdx + 1])
    if 0 < idx:
        positions[2] = int(my_list[idx - 1][jdx])
    if idx + 1 < len(my_list):
        positions[3] = int(my_list[idx + 1][jdx])
    return positions


def startSearch(my_list, lowest_point):
    size_counter = [0]
    check_neighbors(lowest_point, my_list, size_counter)
    return size_counter


def check_neighbors(lowest_point, my_list, size_counter):
    if my_list[lowest_point[0]][lowest_point[1]] != 9:
        my_list[lowest_point[0]][lowest_point[1]] = 9
        size_counter[0] = (size_counter[0] + 1)

        # left right top down
        neighbors = get_neighbors(lowest_point[0], lowest_point[1], my_list)
        if neighbors[0] < 9:
            check_neighbors((int(lowest_point[0]), int(lowest_point[1] - 1)), my_list, size_counter)
        if neighbors[1] < 9:
            check_neighbors((int(lowest_point[0]), int(lowest_point[1] + 1)), my_list, size_counter)
        if neighbors[2] < 9:
            check_neighbors((int(lowest_point[0] - 1), int(lowest_point[1])), my_list, size_counter)
        if neighbors[3] < 9:
            check_neighbors((int(lowest_point[0] + 1), int(lowest_point[1])), my_list, size_counter)


def part_two(my_list, lowest_points):
    basin = []
    for lowest_point in lowest_points:
        if my_list[lowest_point[0]][lowest_point[1]] != 9:
            size = startSearch(my_list, lowest_point)
            basin.append(size[0])

    basin.sort()
    print(basin)
    print(basin[len(basin) - 1] * basin[len(basin) - 2] * basin[len(basin) - 3])


def main():
    my_list = input_file('input3.txt')
    lowest_points = (part_one(my_list))
    part_two(my_list, lowest_points)


main()
