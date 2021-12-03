lines = []
def input_file(filename):
    coefficients = []
    with open(filename,'rt') as file:
        for line in file: # loop over each line
            coefficients.append(str(line).strip()) # parse them in some way
    return coefficients

lines = input_file('day3_input.txt')

my_dict = {}


for idx in range(0, len(lines)):
    split_binary = list(lines[idx])
    for jdx in range(0, len(split_binary)):
        if 'position'+str(jdx) in my_dict:
            my_dict['position'+str(jdx)].append(split_binary[jdx])
        else:
            my_dict['position'+str(jdx)] = []
            my_dict['position'+str(jdx)].append(split_binary[jdx])

gamma_rate = ''
epsilon_rate = ''
for position, value in my_dict.items():
    gamma_rate += (max(set(value), key = value.count)) 
    epsilon_rate += (min(set(value), key = value.count)) 

gamma_num = int(gamma_rate, 2)
epsilon_num = int(epsilon_rate, 2)

print(epsilon_num*gamma_num)


#gamma_num = int(gamma_rate, 2)
#print(gamma_num)
#gamma_num_back2bin = bin(gamma_num)
#epsilon_rate = ~gamma_num_back2bin
#epsilon_num = int(epsilon_rate)
#print(epsilon_num)
