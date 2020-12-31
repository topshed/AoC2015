instructions = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        for c in line:
            instructions.append(c)

floor = 0
for i in instructions:
    if i == "(":
        floor+=1
    elif i == ")":
        floor-=1
print(floor)

