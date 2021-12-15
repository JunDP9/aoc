import copy
from collections import Counter


def input_file(filename):
    nodes = {}
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            line_string = (line.strip().split('-'))

            if line_string[0] in nodes:
                nodes[line_string[0]].append(line_string[1])
            else:
                nodes[line_string[0]] = []
                nodes[line_string[0]].append(line_string[1])

            if line_string[1] in nodes:
                nodes[line_string[1]].append(line_string[0])
            else:
                nodes[line_string[1]] = []
                nodes[line_string[1]].append(line_string[0])
    print(nodes)
    return nodes


def seek_paths(nodes, current_route, node_key, possible_routes):
    for node in nodes[node_key]:
        if node == 'start':
            continue
        if node == 'end':
            current_route.append(node)
            possible_routes.append(current_route)
            continue
        if (node.islower() and node not in current_route) or node.isupper():
            copied_current_route = copy.deepcopy(current_route)
            copied_current_route.append(node)
            seek_paths(nodes, copied_current_route, node, possible_routes)


def seek_paths_improved(nodes, current_route, node_key, possible_routes):
    for node in nodes[node_key]:
        counter = Counter(current_route)
        may_visit = small_cave_counter(dict(counter))
        if node == 'start':
            continue
        if node == 'end':
            current_route.append(node)
            possible_routes.append(current_route)
            continue
        if node.isupper():
            copy_and_continue(current_route, node, nodes, possible_routes)
        if node.islower():
            if node not in current_route:
                copy_and_continue(current_route, node, nodes, possible_routes)
            elif counter[node] < 2 and may_visit:
                copy_and_continue(current_route, node, nodes, possible_routes)


def copy_and_continue(current_route, node, nodes, possible_routes):
    copied_current_route = copy.deepcopy(current_route)
    copied_current_route.append(node)
    seek_paths_improved(nodes, copied_current_route, node, possible_routes)


def small_cave_counter(visited_amount):
    filtered_visited_amount_by_lower = {k: v for (k, v) in visited_amount.items() if k.islower() and (k != 'end' and k != 'start')}
    filtered_visited_amount_by_value = {k: v for (k, v) in filtered_visited_amount_by_lower.items() if v > 1}
    return True if len(filtered_visited_amount_by_value) == 0 else False


def part_one(nodes):
    possible_routes = []
    current_route = ['start']
    seek_paths(nodes, current_route, 'start', possible_routes)


def part_two(nodes):
    possible_routes = []
    current_route = ['start']
    seek_paths_improved(nodes, current_route, 'start', possible_routes)
    print(len(possible_routes))


def main():
    nodes = input_file('input.txt')
    part_one(nodes)
    part_two(nodes)


main()
