import itertools

conts = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        conts.append(int(line))
d = {}
count = 0
min_num = len(conts)
for i in range(len(conts)):
    subcount = 0
    for c in itertools.combinations(conts,i):
        if sum(c) == 150:
            count+=1
            subcount+=1
    d[i] = subcount

print(d)