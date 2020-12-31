grid = []
size = 1000
for y in range(size):
    grid.append(size *['off'])
#print(grid)

def count_on(grid):
    total = 0
    for x in grid:
        #print(x)
        for y in x:
            #print(y)
            if y == 'on':
                total+=1
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
                    grid[x][y] = state
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

                    if grid[x][y] == 'on':
                        grid[x][y] = 'off'
                    else:
                        grid[x][y] = 'on'
print(count_on(grid))