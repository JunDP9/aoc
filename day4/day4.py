import math
import numpy as np

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
#print(lines)

def get_new_node(number):
    return [number, 0]

def get_new_node_dict(number):
    return dict([(str(number), 0)])

def prepare_input(board_size, input_list):
    boards = {}
    boards_amt_bingo = {}
    for idx in range(0, len(input_list)):
        nums = [int(n) for n in input_list[idx].split()]
        if ('board '+str(math.ceil(idx/board_size)) not in boards_amt_bingo):
            boards_amt_bingo['board '+str(math.ceil(idx/board_size))] = 0

        for number in nums:
            if 'board '+str(math.ceil(idx/board_size)) in boards:
                boards['board '+str(math.ceil(idx/board_size))].append(get_new_node_dict(int(number)))
            else:
                boards['board '+str(math.ceil(idx/board_size))] = []
                boards['board '+str(math.ceil(idx/board_size))].append(get_new_node_dict(int(number)))
    return [boards, boards_amt_bingo]  


def prepare_array(board_size, input_list):
    boards = {}
    board_counter = 0
    for idx in range(0, len(input_list)):
        nums = [int(n) for n in input_list[idx].split()]
        if idx % board_size == 0:
            board_counter += 1
        for number in nums:
            if 'board '+str(board_counter) in boards:
                boards['board '+str(board_counter)].append(get_new_node(int(number)))
            else:
                boards['board '+str(board_counter)] = []
                boards['board '+str(board_counter)].append(get_new_node(int(number)))

    return boards  

    

boards = prepare_input(5, lines)[0]
boards_array = prepare_array(5, lines)
boards_amt_bingo = prepare_input(5, lines)[1]

def check_bingo(board):
    board_size = 5 - 1
    board_col_counter = board_size + 1
    for idx in range(0, len(board)):
        

        if board_col_counter  > board_size: #and idx < len(board)-board_size:
            #print('row ' + str(idx))
            row = (board[idx:board_size+1+idx])

            hor_flag = True
            for number in row:
                if(number[1] == 1):
                    hor_flag = True
                else:
                    hor_flag = False
                    break
            if hor_flag == True:
                print('row')
                print(row)

                return True
            
            board_col_counter = 0
        board_col_counter+=1

    for jdx in range(0, (board_size+1)):
        col = []
        for kdx in range(0, (board_size+1)):
            col.append(board[jdx+(kdx*(board_size+1))])
        hor_flag = True
        for number in col:
            if(number[1] == 1):
                hor_flag = True
            else:
                hor_flag = False
                break
        if hor_flag == True:
            print('col')
            print(col)
            return True

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
                    boards_amt_bingo[key] += 1
                    #break
                #if idx > 4 and boards_amt_bingo[key] > 4:
                    if check_bingo(value) == True:
                        print(key)
                        print(value)
                        calculate_final(bingo_numbers[idx], value)
                        return

main(bingo_numbers, boards_array, boards_amt_bingo)
                

    

        
        
    

