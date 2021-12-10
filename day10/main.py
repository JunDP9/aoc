def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients.append((str(line).strip()))  # parse them in some way
    return list(coefficients)


def part_one(my_list):
    lookup_table = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
    total_sum = 0
    incomplete_lines = []
    for line in my_list:
        my_stack = []
        for char in line:
            if char not in lookup_table:
                my_stack.append(char)
            else:
                if my_stack[len(my_stack) - 1] == lookup_table[char][0]:
                    my_stack.pop()
                else:
                    total_sum += lookup_table[char][1]
                    my_stack = []
                    break
        if my_stack:
            incomplete_lines.append(my_stack)

    print(total_sum)
    return incomplete_lines


def part_two(incomplete_stacks):
    lookup_table = {'(': 1, '[': 2, '{': 3, '<': 4}
    final_amount = []
    for incomplete_stack in incomplete_stacks:
        incomplete_stack.reverse()
        total_stack_amount = 0
        for char in incomplete_stack:
            total_stack_amount = total_stack_amount * 5
            total_stack_amount += lookup_table[char]
        final_amount.append(total_stack_amount)
    final_amount.sort()

    print(final_amount[int(((len(final_amount) - 1) / 2))])


def main():
    my_list = input_file('input.txt')
    incomplete_lines = (part_one(my_list))
    part_two(incomplete_lines)


main()
