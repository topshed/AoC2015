regs = {}
wiring = []
with open("input.txt") as file:
    for line in file:
        #print(line)
        line = line.strip().split(" ")
        wiring.append(line)

#print(wiring)

'''for line in wiring:
        if len(line) == 3:
            in1 = int(line[0])
            output = line[2]
            op = line[1]
            regs[output] = in1'''

print(regs)
to_be_processed = []
while len(to_be_processed) != len(wiring):
    for line in wiring:
            #print(line)
            process = False
            if line not in to_be_processed:
                if len(line) == 5:
                    in1 = line[0]
                    op = line[1]
                    in2 = line[2]
                    output = line[4]
                    if (in1 in regs and in2 in regs) or (in1 in regs and in2.isnumeric()) or (in2 in regs and in1.isnumeric()):
                        process = True
                elif len(line) == 3:
                    in1 = line[0]
                    output = line[2]
                    op = line[1]
                    if in1.isnumeric():
                        regs[output] = int(in1)
                        to_be_processed.append(line)
                    else:
                        if in1 in regs:
                            to_be_processed.append(line)
                            regs[output] = regs[in1]

                elif len(line) == 4:
                    in1 = line[1]
                    op = line[0]
                    output = line[3] 
                    if in1 in regs:
                        process = True
                else:
                    print("dunno")
                if process:
                    to_be_processed.append(line)
                    if op == "->":
                        regs[output] = in1
                    elif op == "AND":
                        if in1.isnumeric():
                            regs[output] = int(in1) & regs[in2]
                        else:
                            regs[output] = regs[in1] & regs[in2]
                    elif op == "OR":
                        regs[output] = regs[in1] | regs[in2]
                    elif op == "LSHIFT":
                        regs[output] = regs[in1] << int(in2) 
                    elif op == "RSHIFT":
                        regs[output] = regs[in1] >> int(in2) 
                    elif op == "NOT":
                        regs[output] = ~ regs[in1]
    print(len(wiring), len(to_be_processed))
    #print(regs)

print(regs['a'])
#print(regs)

#regs['b'] = regs['a']
regs = {'b':regs['a']}
print(regs)
to_be_processed = []
while len(to_be_processed) != len(wiring)-1:
    for line in wiring:
            #print(line)
            process = False
            if line not in to_be_processed:
                if len(line) == 5:
                    in1 = line[0]
                    op = line[1]
                    in2 = line[2]
                    output = line[4]
                    if (in1 in regs and in2 in regs) or (in1 in regs and in2.isnumeric()) or (in2 in regs and in1.isnumeric()):
                        process = True
                elif len(line) == 3:
                    in1 = line[0]
                    output = line[2]
                    op = line[1]
                    if output != 'b':
                        if in1.isnumeric():
                            regs[output] = int(in1)
                            to_be_processed.append(line)
                        else:
                            if in1 in regs:
                                to_be_processed.append(line)
                                regs[output] = regs[in1]

                elif len(line) == 4:
                    in1 = line[1]
                    op = line[0]
                    output = line[3] 
                    if in1 in regs:
                        process = True
                else:
                    print("dunno")
                if process:
                    to_be_processed.append(line)
                    if op == "->":
                        regs[output] = in1
                    elif op == "AND":
                        if in1.isnumeric():
                            regs[output] = int(in1) & regs[in2]
                        else:
                            regs[output] = regs[in1] & regs[in2]
                    elif op == "OR":
                        regs[output] = regs[in1] | regs[in2]
                    elif op == "LSHIFT":
                        regs[output] = regs[in1] << int(in2) 
                    elif op == "RSHIFT":
                        regs[output] = regs[in1] >> int(in2) 
                    elif op == "NOT":
                        regs[output] = ~ regs[in1]

print(regs['a'])
