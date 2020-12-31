grid = []
size = 1000
for y in range(size):
    grid.append(size *[0])
#print(grid)

def sum_bright(grid):
    total = 0
    for x in grid:
        #print(x)
        for y in x:
            #print(y)
            total= total + y
    return(total)

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        op = line[0]
        if op != 'toggle':
            state = line[1]
            start = line[2]
            start_x = int(start.split(",")[0])
            start_y = int(start.split(",")[1])
            stop = line[4]
            stop_x = int(stop.split(",")[0])
            stop_y = int(stop.split(",")[1])
            #print(start_x, stop_x, start_y, stop_y,state)
            for y in range(start_y, stop_y+1):
                for x in range(start_x, stop_x+1):
                    #print("turning", x,y,state)
                    if state == 'on':
                        grid[x][y] = grid[x][y] + 1
                    elif state == 'off':
                        if grid[x][y] >=1:
                            grid[x][y] = grid[x][y] - 1
        else:
            start = line[1]
            stop = line[3]
            start_x = int(start.split(",")[0])
            start_y = int(start.split(",")[1])
            stop_x = int(stop.split(",")[0])
            stop_y = int(stop.split(",")[1])
            #print(start_x, stop_x, start_y, stop_y)
            for y in range(start_y, stop_y+1):
                for x in range(start_x, stop_x+1):
                    grid[x][y] = grid[x][y] +2
print("calc")
print(sum_bright(grid))