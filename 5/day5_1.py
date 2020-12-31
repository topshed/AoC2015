import re
import string
def countVowels(string):
    vowels = "aeiou"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

repeated = []
for c in string.ascii_lowercase:
    repeated.append(c+c)

bad = ["ab", "cd", "pq", "xy"]

print(repeated)
total = 0 
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        print("checking vowels")
        if countVowels(line) >=3:
            print(">=3 vowels")
            doubles = False
            print("checking doubles")
            for check in repeated:
                #print("checking", check)
                if re.search(check,line) != None:
                    print("found",check)
                    doubles = True
                    break
            bads = False
            print("checking bads")
            for check in bad:
                #print("checking", check)
                if re.search(check,line) != None:
                    print("found", check)
                    bads = True
                    break
            if doubles and not bads:
                print("nice word") 
                total+=1
print(total)        
                






