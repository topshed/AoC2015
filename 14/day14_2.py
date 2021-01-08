from collections import defaultdict
reindeer_paras = defaultdict(dict)
#race = 1000
race = 1
with open('input.txt') as file:
    for line in file:
        line = line.strip().strip(".").split()
        name = line [0]
        speed = int(line[3])
        duration = int(line[6])
        rest = int(line[13])
        reindeer_paras[name] = {'speed': speed, 'duration': duration, 'rest': rest, 'points':0}

def in_lead(d):
    dist = 0
    for r in d:
        if dist < d[r]['travelled']:
            dist = d[r]['travelled']
            winner = r
    return winner


for race in range(1,2504):
    for r in reindeer_paras:
        total = 0
        reindeer_paras[r]['chunk'] = reindeer_paras[r]['duration'] + reindeer_paras[r]['rest']
        steps = race//reindeer_paras[r]['chunk']
        
        leftover = race - (steps * reindeer_paras[r]['chunk'] )
        #print(steps,leftover)
        if leftover > reindeer_paras[r]['duration']:
            #print("full sess")
            total = (steps * reindeer_paras[r]['speed'] * reindeer_paras[r]['duration']) + (reindeer_paras[r]['speed'] * reindeer_paras[r]['duration'])
        else:
            total = (steps * reindeer_paras[r]['speed'] * reindeer_paras[r]['duration']) + (leftover * reindeer_paras[r]['speed'])
        reindeer_paras[r]['travelled'] = total
    w = in_lead(reindeer_paras)
    print(w)
    reindeer_paras[w]['points']+=1
    print(reindeer_paras)
furthest = 0
for r in reindeer_paras:
    if furthest < reindeer_paras[r]['travelled']:
        furthest = reindeer_paras[r]['travelled']
print(furthest)
