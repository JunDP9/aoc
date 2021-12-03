lines = []
with open('day1_input.txt') as f:
    lines = f.readlines()

converted_list = []

for element in lines:
    converted_list.append(element.strip())

res = []
for idx in range(1, len(converted_list)):
    if converted_list[idx - 1] < converted_list[idx]:
        res.append("Increased")
    else:
        res.append("Decreased")

increased = filter(lambda status: status == "Increased", res)
print(len(list(increased)))
