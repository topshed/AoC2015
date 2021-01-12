row = 2981
column  = 3075
for x in range(1,7):
    for y in range(1,7):
        val = (((y+(x-1))**2)/2 - (y+(x-1))/2) + x
        val2 = ((y + x - 2) * ((y + x - 2) + 1)) / 2 + x - 1 
        print(x,y,int(val), int(val2))


n = row + column - 2
iterations = (n * (n + 1)) / 2 + column - 1