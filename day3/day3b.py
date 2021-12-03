lines = []
def input_file(filename):
    coefficients = []
    with open(filename,'rt') as file:
        for line in file: # loop over each line
            coefficients.append(str(line).strip()) # parse them in some way
    return coefficients

lines = input_file('day3_input.txt')
     
def get_amount_one_zero(filtered_list, index):
    amount_0 = 0
    amount_1 = 0
    for binary in filtered_list:
        if(list(binary)[index]=='1'): 
            amount_1+=1
        else:
            amount_0+=1
    return [amount_0, amount_1]

def determine_most_bits(filtered_list, index):
    amount_0 = get_amount_one_zero(filtered_list, index)[0]
    amount_1 = get_amount_one_zero(filtered_list, index)[1]
    if amount_0 > amount_1:
        return '0'
    if amount_0 < amount_1:
        return '1'
    if amount_0 == amount_1:
        return '1'

def determine_less_bits(filtered_list, index):
    if determine_most_bits(filtered_list, index) == '1':
        return '0'
    return '1'

filtered_gamma = []
filtered_epsilon = []

for jdx in range(0, len(lines[0])):
    if jdx == 0:
        filtered_gamma = list(filter(lambda x : list(x)[jdx] ==(determine_most_bits(filtered_gamma, jdx)), lines))
        filtered_epsilon = list(filter(lambda x : list(x)[jdx] == (determine_less_bits(filtered_gamma, jdx)), lines))

    else:
        if len(filtered_gamma) > 1 :
            filter_bit_gamma = (determine_most_bits(filtered_gamma, jdx))        
            filtered_gamma = list(filter(lambda x : list(x)[jdx] == filter_bit_gamma, filtered_gamma))
        if len(filtered_epsilon) > 1 :
            filter_bit_epsilon = (determine_less_bits(filtered_epsilon, jdx))        
            filtered_epsilon = list(filter(lambda x : list(x)[jdx] == filter_bit_epsilon, filtered_epsilon))


gamma_num = int(filtered_gamma[0], 2)
epsilon_num = int(filtered_epsilon[0], 2)
print(epsilon_num*gamma_num)
