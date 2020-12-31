import re
import string
def countVowels(string):
    vowels = "aeiou"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

total = 0 
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        print(line)
        doubles = False
        print("checking repeats")
        if re.search(r"(\w{2}).*?(\1)",line) != None:
            print("found repeat")
            doubles = True
        betweens = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                betweens = True
        if doubles and betweens:
            print("nice word") 
            total+=1
print(total)        
                






