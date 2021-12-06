def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients = (str(line)
                            .replace(',', ' ')
                            )  # parse them in some way
    return coefficients


def grow(mydict, mylist, amount_days):
    for idx in range(0, amount_days):
        for key, value in mydict.items():
            if key is not -1:
                mydict[(int(key) - 1)] = value

        mydict[8] = mydict[(-1)]
        mydict[6] = mydict[6] + mydict[(-1)]
        mydict[(-1)] = 0

    return mylist


def main():
    line = input_file('input.txt')
    mylist = [int(x) for x in line.split(' ')]
    mydict = {}
    init_dict(mydict, mylist)

    print(sum(mydict.values()))
    grow(mydict, mylist, 256)
    print(sum(mydict.values()))


def init_dict(mydict, mylist):
    for idx in range(-1, 9):
        mydict[idx] = mylist.count(idx)

main()
