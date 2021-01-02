inp = "1113122113"

def look_and_say(inp):
    new_seq = ""
    m = 1
    if len(inp) == 1:
        new_seq = str(1) + inp
    else:
        for i in range(len(inp)-1):
            #print(inp[i])
            if inp[i] == inp[i+1]:
                m+=1
            else:
                new_seq = new_seq + str(m) + inp[i]
                m = 1
        new_seq = new_seq + str(m) + inp[i+1]

    return(new_seq)

for i in range(50):
    print(i,len(inp))
    inp = look_and_say(inp)
#print(inp)
print(len(inp))
'''311311222113
13211321322113
13211321322113
1113122113121113222113
1113122113121113222113
31131122211311123113322113
31131122211311123113322113'''