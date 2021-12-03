lines = []
converted_list = []
with open('day1_input.txt') as f:
    lines = f.readlines()
for element in lines:
    converted_list.append(element.strip())

d = []
for idx in range(1, len(converted_list)-2):
  d.append(int(converted_list[idx]) + int(converted_list[idx+1]) + int(converted_list[idx+2]))

res = []
for idx in range(1, len(d)):
    if d[idx - 1] < d[idx]:
        res.append("Increased")
    else:
        res.append("Decreased")

increased = filter(lambda status: status == "Increased", res)
print(len(list(increased)))