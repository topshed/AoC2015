import re
'''import json
with open("input.txt") as file:
    data = json.load(file)'''

total =0
with open("input.txt") as f:
    for line in f:
        nums = re.findall('-?\d+\.?\d*',line)
        for i in nums:
            total = total + int(i)

print(total)   
# 417209
# (^[-+]?([0-9]+)(\.[0-9]+)?)$'