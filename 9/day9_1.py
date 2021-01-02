from collections import defaultdict
from itertools import permutations

cities = defaultdict(dict)

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        start_city, _, end_city, _, distance = line
        cities[start_city][end_city] = int(distance)
        cities[end_city][start_city] = int(distance)

print(cities)
total_dist = []
for x in permutations(cities.keys()):
    print("x", x)
    total = 0
    for y in range(len(x)-1):
        total = total + cities[x[y]][x[y+1]]
    total_dist.append(total)

print(min(total_dist))
#part 2
print(max(total_dist))