import numpy as np


def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients= (str(line)
                                .replace(',', ' ')
                                )  # parse them in some way
    return coefficients

def grow(mylist, amount_days):
    for idx in range(0, amount_days):
        mylist = [item-1 for item in mylist] #subtract 1
        mylist = mylist+([8]*mylist.count(-1))
        mylist = [6 if item == -1 else item for item in mylist]

    print(len(mylist))
    return mylist
        # subtract 1
        # count amount -1
        # add 8 for the counted amount
        # replace all occurences of -1 by 6


def main():
    line = input_file('input2.txt')
    mylist = [int(x) for x in line.split(' ')]
    # test = [0,4,6,3]
    # print(test)
    print(len(mylist))

    grow(mylist, 256)



main()
