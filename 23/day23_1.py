rega = 1
regb = 0
def half(reg):
    return(reg/2)

def triple(reg):
    return(reg*3)

def inc(reg):
    return(reg+1)

prog = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split()
        op = line[0]
        if len(line) == 3:
            reg = line[1].strip(",")
            arg = int(line[2])
        else:
            if op == 'jmp':
                reg = None
                arg = int(line[1])
            else:
                reg = line[1]
        prog.append([op,reg,arg])
print(prog)

i = 0
while i < len(prog):
    print(prog[i],rega,regb)
    if prog[i][0] == 'jmp':    
        i+=prog[i][2]
    else:
        if prog[i][1] == 'a':
            if prog[i][0] == 'hlf':
                rega = half(rega)
                i+=1
            elif prog[i][0] == 'tpl':
                rega = triple(rega)
                i+=1
            elif prog[i][0] == 'inc':
                rega = inc(rega)
                i+=1
            elif prog[i][0] == 'jie':
                if rega%2 == 0 or rega == 0:
                    i+=prog[i][2]
                else:
                    i+=1
            elif prog[i][0] == 'jio':
                if rega == 1:
                    i+=prog[i][2]
                else:
                    i+=1
        elif prog[i][1] == 'b':
            if prog[i][0] == 'hlf':
                regb = half(regb)
                i+=1
            elif prog[i][0] == 'tpl':
                regb = triple(regb)
                i+=1
            elif prog[i][0] == 'inc':
                regb = inc(regb)
                i+=1
            elif prog[i][0] == 'jie':
                if regb%2 == 0 or regb == 0:
                    i+=prog[i][2]
                else:
                    i+=1
            elif prog[i][0] == 'jio':
                if rega == 1:
                    i+=prog[i][2]
                else:
                    i+=1

    

print(rega,regb)