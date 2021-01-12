import re
rep = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if "=>" in line and line != "":
            line = line.split("=>")
            rep.append((line[0].strip(),line[1].strip()))
        else:
            start = line

print(start, rep)


med = start
count = 0
while med != 'e':
    for sub, repl in rep:
        if repl in med:
            med = med.replace(repl, sub, 1)
            count += 1
print(count)


    