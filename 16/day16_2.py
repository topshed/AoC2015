from collections import defaultdict
sues = defaultdict(dict)

the_sue = {"children" :3, "cats" : 7, "samoyeds" : 2, "pomeranians" :3, \
"akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}

with open("input.txt") as file:
    for line in file:
        line = line.strip().split()
        sues[int(line[1].strip(":"))] = {line[2].strip(":"): int(line[3].strip(",")), line[4].strip(":"): int(line[5].strip(",")),line[6].strip(":"): int(line[7].strip(",")) }

#print(sues)

for sue in sues:
    #print(sues[sue])
    match = True
    for mem in sues[sue]:
        if mem == 'trees' or mem == 'cats':
            if sues[sue][mem] > the_sue[mem] or sues[sue][mem] == 0:
                pass
            else:
                match = False
        elif mem == 'pomeranians' or mem == 'goldfish':
            if sues[sue][mem] < the_sue[mem] or sues[sue][mem] == 0:
                pass
            else:
                match = False  
        else:         
            if sues[sue][mem] == the_sue[mem] or sues[sue][mem] == 0:
                pass
                #print("match", sues[sue][mem], the_sue[mem])
            else:
                match = False
                #print("no match", sues[sue][mem], the_sue[mem])
    if match:
        print(sue)