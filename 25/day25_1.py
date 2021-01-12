row = 2981
column  = 3075
'''for x in range(1,7):
    for y in range(1,7):
        val = (((y+(x-1))**2)/2 - (y+(x-1))/2) + x
        print(x,y,int(val))'''

x = column
y = row
val = (((y+(x-1))**2)/2 - (y+(x-1))/2) + x # Jasper worked this out!
print(val)

def gen(start):
    return((start * 252533) % 33554393)

answer = 20151125
for i in range(int(val)-1):
    answer = gen(answer)
print(answer)
