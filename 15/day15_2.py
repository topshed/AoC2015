from collections import defaultdict
ingreds = defaultdict(dict)
with open("input.txt") as file:
    for line in file:
        line = line.strip().split()
        ingreds[line[0]] = {line[1]: int(line[2].strip(',')), line[3]: int(line[4].strip(',')), line[5]: int(line[6].strip(',')), line[7]: int(line[8].strip(',')),line[9]: int(line[10].strip(','))}
k = list(ingreds.keys())
print(ingreds[k[0]]['capacity'])
print(ingreds)
max_score = 0
for a in range(0,100):
    for b in range(0,100-a):
        for c in range(0,100-a-b):
            d = 100 - a - b - c
            total_cap = (ingreds[k[0]]['capacity'] * a) + (ingreds[k[1]]['capacity'] * b) + (ingreds[k[2]]['capacity'] * c) + (ingreds[k[3]]['capacity'] * d)
            #print(ingreds[k[0]]['capacity'],ingreds[k[1]]['capacity'],ingreds[k[2]]['capacity'],ingreds[k[3]]['capacity'])
            if total_cap < 0:
                total_cap = 0
            #print(total_cap)
            total_dur = (ingreds[k[0]]['durability'] * a)+ (ingreds[k[1]]['durability'] * b)+ (ingreds[k[2]]['durability'] * c)+ (ingreds[k[3]]['durability'] * d)
            #print(ingreds[k[0]]['durability'],ingreds[k[1]]['durability'],ingreds[k[2]]['durability'],ingreds[k[3]]['durability'])
            if total_dur < 0:
                total_dur = 0
            total_fla = (ingreds[k[0]]['flavor'] * a)+ (ingreds[k[1]]['flavor'] * b)+ (ingreds[k[2]]['flavor'] * c)+ (ingreds[k[3]]['flavor'] * d)
            if total_fla < 0:
                total_fla = 0
            total_tex = (ingreds[k[0]]['texture'] * a)+ (ingreds[k[1]]['texture'] * b)+ (ingreds[k[2]]['texture'] * c)+ (ingreds[k[3]]['texture'] * d)
            if total_tex < 0:
                total_tex = 0
            total_cal = (ingreds[k[0]]['calories'] * a)+ (ingreds[k[1]]['calories'] * b)+ (ingreds[k[2]]['calories'] * c)+ (ingreds[k[3]]['calories'] * d)
            if total_cal < 0:
                total_cal = 0
            total = total_cap * total_dur * total_fla * total_tex
            print(a,b,c,d,total_cap, total_dur, total_fla, total_tex,total)
            if total_cal == 500:
                if total > max_score:
                    max_score = total
print(max_score)