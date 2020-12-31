regs = {}
with open("input.txt") as file:
    for line in file:
        print(line)
        line = line.strip().split(" ")
        if len(line) == 3:
            in1 = int(line[0])
            output = line[2]
            op = line[1]
        elif len(line) == 5:
            in1 = line[0]
            op = line[1]
            in2 = line[2]
            output = line[4] 
        elif len(line) == 4:
            in1 = line[1]
            op = line[0]
            output = line[3] 
        else:
            print("dunno")
        if op == "->":
            regs[output] = in1
        elif op == "AND":
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

'''p LSHIFT 2 -> q 
means that the value from wire p is left-shifted by 2 and then provided to wire q.'''