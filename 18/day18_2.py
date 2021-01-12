import copy
size = 100
grid = []
grid.append(["."] * (size+2))

def find_adj(x,y):
    adj = []
    for i in range(-1,2):
         for j in range(-1,2):
            adj.append((x+j,y+i))
    adj.remove((x,y))
    return(adj)


def count_on(grid):
    total = 0
    for x in grid:
        #print(x)
        for y in x:
            #print(y)
            if y == '#':
                total+=1
    return(total)

def print_grid(g):
    for r in g:
        s = ""
        for p in r:
            s = s + p
        print(s)
    print("")

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        row = ["."]
        for y in range(len(line)):
            row.append(line[y])
        row.append(".")
        grid.append(row)
grid.append(["."] *(size+2))

#print(len(line))
print(len(grid),len(grid[0]))
#print(grid[0][0])
#print(find_adj(50,50))  
grid[1][len(grid)-2] = '#'   
grid[1][1] = '#' 
grid[len(grid)-2][1] = '#'   
grid[len(grid)-2][len(grid)-2] = '#' 
print_grid(grid) 

for i in range(100):
    #print(i,grid)
    new_grid = copy.deepcopy(grid)
    for row in range(1,len(grid)-1):
        for light in range(1,len(grid[row])-1):
            #print(row,light)
            count = 0
            #print(find_adj(row,light),grid[row][light])
            for light_adj in find_adj(row,light):
                #print(grid[light_adj[0]][light_adj[1]])
                #print(light_adj)
                if grid[light_adj[0]][light_adj[1]] == '#':
                    #print("hit", light_adj,grid[light_adj[0]][light_adj[1]])
                    count +=1
            #print("count",count)
            if grid[row][light] == '#':
                if count == 3 or count == 2:
                    new_grid[row][light] = '#'
                    #print("turning on")
                else:
                    new_grid[row][light] = '.'
                    #print("turning off")
            else:
                if count == 3:
                    new_grid[row][light] = '#'
                    #print("turning on")
    grid = new_grid
    grid[1][len(grid)-2] = '#'   
    grid[1][1] = '#' 
    grid[len(grid)-2][1] = '#'   
    grid[len(grid)-2][len(grid)-2] = '#'        
    #print_grid(grid)

print(count_on(grid))
'''op = line[0]
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
print(count_on(grid))'''