from collections import defaultdict
from itertools import permutations
happy = defaultdict(dict)
with open("input.txt") as file:
    for line in file:
        line = line.strip().strip(".").split()
        person = line[0]
        val = int(line[3])
        next_to = line[10]
        mode = line[2]
        if mode == 'lose':
            val = val * -1
        happy[person][next_to] = val


everyone = set(happy.keys())
for e in everyone:
    happy['me'][e] = 0
    happy[e]['me'] = 0
    print(e)
#print(everyone)
#print(happy)
perm = permutations(happy.keys())
max = 0
best = None
for seating_arrangement in list(perm):
    total = 0
    for place in range(len(seating_arrangement)):
        #print(place)
        if place == len(seating_arrangement) - 1:
            cw_neighbour = 0
        else:
            cw_neighbour = place + 1
        #print(neighbour)
        #for h in happy[seating_arrangement[place]].keys():
         #   print(happy[seating_arrangement[place]]['Bob'])
        #print(happy[seating_arrangement[place]]['Bob'])
        unit = happy[seating_arrangement[place]][seating_arrangement[cw_neighbour]]
        total = total + unit
        if place == 0:
            ccw_neighbour = len(seating_arrangement) -1
        else:
            ccw_neighbour = place - 1
        unit = happy[seating_arrangement[place]][seating_arrangement[ccw_neighbour]]
        total = total + unit
        #print(seating_arrangement, total)
        if total > max:
            best = seating_arrangement
            max = total
print(best, max )