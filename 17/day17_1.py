import itertools

conts = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        conts.append(int(line))
count = 0
for i in range(len(conts)):
    for c in itertools.combinations(conts,i):
        if sum(c) == 150:
            count+=1

print(count)