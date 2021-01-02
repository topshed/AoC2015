total = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        print(line)
        total += line.count('\\') + line.count('"') + 2
        # every encoded string will have 2 more chars ( for the double-quotes at)
        # each end, plus one extra for every other double-quote and one extra
        # for every slash (which is escaped in the count parameter)

print(total)