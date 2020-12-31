instructions = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        for c in line:
            instructions.append(c)

floor = 0
c = 1
for i in instructions:
    if floor == -1:
        print(c)
    if i == "(":
        floor+=1
    elif i == ")":
        floor-=1
    c+=1
print(floor)

