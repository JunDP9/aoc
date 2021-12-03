lines = []
with open('day2_input.txt') as f:
    lines = f.readlines()

converted_list = []

for element in lines:
    converted_list.append(element.strip())

def x_direction(x, amount):
    x = x + amount
    return x

def y_direction_down(y, amount):
    y = y + amount
    return y 

def y_direction_up(y, amount):
    y = y - amount
    return y 

def createCommands(): 
    dict = {
        "forward": x_direction,
        "up": y_direction_up,
        "down": y_direction_down
    }
    return dict

commands = createCommands()
x = 0
y = 0 

for line in converted_list:
    if(line.split()[0]=="forward"):
        x = commands["forward"](x, int(line.split()[1]))
    else:
        y = commands[line.split()[0]](y, int(line.split()[1]))

print(x, y)
print(x*y)