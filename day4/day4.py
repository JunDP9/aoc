import math

lines = []
def input_file(filename):
    coefficients = []
    with open(filename,'rt') as file:
        for line in file: # loop over each line
            if str(line) !='':
                coefficients.append(str(line).strip()) # parse them in some way
    return coefficients

lines = input_file('input.txt')
lines = list(filter(None, lines))

bingo_numbers=lines[0].split(",")
lines.pop(0)

def get_new_node(number):
    return [number, 0]

def prepare_array(board_size, input_list):
    boards = {}
    boards_amt_bingo = {}
    board_counter = 0
    for idx in range(0, len(input_list)):
        nums = [int(n) for n in input_list[idx].split()]
        if ('board '+str(math.ceil(idx/board_size)) not in boards_amt_bingo):
            boards_amt_bingo['board '+str(math.ceil(idx/board_size))] = 0

        if idx % board_size == 0:
            board_counter += 1
        for number in nums:
            if 'board '+str(board_counter) in boards:
                boards['board '+str(board_counter)].append(get_new_node(int(number)))
            else:
                boards['board '+str(board_counter)] = []
                boards['board '+str(board_counter)].append(get_new_node(int(number)))

    return [boards, boards_amt_bingo]   

boards_array = prepare_array(5, lines)[0]
boards_amt_bingo = prepare_array(5, lines)[1]

def check_bingo(board):
    board_size = 5 - 1
    board_col_counter = board_size + 1
    for idx in range(0, len(board)):
        if board_col_counter  > board_size: 
            row = (board[idx:board_size+1+idx])
            col = []
            for kdx in range(0, (board_size+1)):
                col.append(board[math.floor(idx/(board_size+1))+(kdx*(board_size+1))])
            flat_row_list = [item for sublist in row for item in sublist[1:]]
            flat_col_list = [item for sublist in col for item in sublist[1:]]
            if 0 not in flat_row_list or 0 not in flat_col_list:
                return True
            board_col_counter = 0
        board_col_counter+=1
    return False

def calculate_final(final_number, board):
    sum = 0
    for number in board:
        if str(number[1]) == '0':
            sum += number[0]
    print('final number '+ str(final_number))
    print('sum '+ str(sum))
    print('end '+str(int(final_number)*sum))
          
def main(bingo_numbers, boards_array, boards_amt_bingo):
    for idx in range(0, len(bingo_numbers)):
        for key, value in boards_array.items():
            # value is a board
            for number in value: 
                if int(bingo_numbers[idx]) == int(number[0]):
                    number[1] = 1
                    if check_bingo(value) == True:
                        print(key)
                        boards_amt_bingo.pop(key, None) 
                        calculate_final(bingo_numbers[idx], value)
                        return



            


main(bingo_numbers, boards_array, boards_amt_bingo)
                

    

        
        
    

