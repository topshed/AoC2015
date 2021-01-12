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

def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

after_rep = []
for job in rep:
    #print(job)
    sub = job[0]
    repl = job[1]
    print(sub,repl)
    n_hits = len(re.findall(sub,start))

    for i in range(n_hits):
        after_rep.append(nth_repl(start,sub,repl,i+1))

print(after_rep)
print(len(set(after_rep)))
    