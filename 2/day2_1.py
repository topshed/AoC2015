total = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip().split("x")
        print(line)
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        dims = [l,w,h]
        slack1 = min(dims)
        dims.remove(slack1)
        slack2 = min(dims)
        #2*l*w + 2*w*h + 2*h*l
        total = total + ((2*l*w)+ (2*w*h) + (2*h*l)) + (slack1*slack2)
print(total)

