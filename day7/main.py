import operator
def input_file(filename):
    coefficients = []
    with open(filename, 'rt') as file:
        for line in file:  # loop over each line
            coefficients = (str(line)
                            .replace(',', ' ')
                            )  # parse them in some way
    return coefficients


def getLowestValue(mydict):
    sums = []
    for key, value in mydict.items():
        sums.append(sum(value))
    min_index, min_value = min(enumerate(sums), key=operator.itemgetter(1))
    max_index, max_value = max(enumerate(sums), key=operator.itemgetter(1))

    print(min_index)
    print(min_value)
    print(max_index)
    print(max_value)
    pass


def main():
    line = input_file('input2.txt')
    mylist = [int(x) for x in line.split(' ')]
    mydict = {}
    calc_dict(mydict, mylist)
    getLowestValue(mydict)


def calc_dict(mydict, mylist):
    for idx in range(0, len(mylist)):
        for jdx in range(0, len(mylist)):
            if 'position '+str(idx) in mydict:
                mydict['position '+str(idx)].append(abs(mylist[idx]-mylist[jdx]))
            else:
                mydict['position '+str(idx)] = []
                mydict['position '+str(idx)].append(abs(mylist[idx]-mylist[jdx]))

main()
