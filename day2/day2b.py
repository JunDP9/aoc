lines = []
with open('day2_input.txt') as f:
    lines = f.readlines()

converted_list = []

for element in lines:
    converted_list.append(element.strip())

def go_forward(x, aim, y, amount):
    x = x + amount
    y = y + (amount * aim)
    return [x, y]

def go_down(aim, amount):
    aim = aim + amount
    return aim 

def go_up(aim, amount):
    aim = aim - amount
    return aim 

def createCommands(): 
    commands = {
        "forward": go_forward,
        "up": go_up,
        "down": go_down
    }
    return commands

commands = createCommands()
x = 0
y = 0 
aim = 0

for line in converted_list:
    if(line.split()[0]=="forward"):
        x = commands["forward"](x, aim, y, int(line.split()[1]))[0]
        y = commands["forward"](x, aim, y, int(line.split()[1]))[1]
    else:
        aim = commands[line.split()[0]](aim, int(line.split()[1]))

print(("positions: {}, {}").format(x,y))
print("part 2 solution: " + str(x*y))