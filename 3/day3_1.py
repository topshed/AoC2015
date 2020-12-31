with open("input.txt") as file:
    for line in file:
        line = line.strip()

visited = [[0,0]]
pos = [0,0]
pos_r = [0,0]
robo = 1
#line = "^v^v^v^v^v"
for c in line:
    if robo % 2 != 0:
        print("robo")
        if c == ">":
            pos[0]+=1
        elif c == "<":
            pos[0]-=1
        elif c == "^":
            pos[1]+=1
        elif c == "v":
            pos[1]-=1
        if [pos[0],pos[1]] not in visited:
            print("new")
            visited.append([pos[0],pos[1]])
    else:
        print("santa")
        if c == ">":
            pos_r[0]+=1
        elif c == "<":
            pos_r[0]-=1
        elif c == "^":
            pos_r[1]+=1
        elif c == "v":
            pos_r[1]-=1
        if [pos_r[0],pos_r[1]] not in visited:
            print("new")
            visited.append([pos_r[0],pos_r[1]])
    robo+=1

print(len(visited))