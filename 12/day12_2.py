import json


#print(json.dumps(data,sort_keys=True,indent=4))


def sum_no_reds(data):
    if type(data) is int:
        print("int")
        return data
    if type(data) is list:
        return sum(map(sum_no_reds, data))
        print("list")
    if type(data) is dict:
        vals = data.values()
        print("dict")
        if "red" in vals:
            return 0
        return sum(map(sum_no_reds, vals))
    else:
        print("dunno")
        return 0

with open("input.txt") as file:
    data = json.load(file)
    print(sum_no_reds(data)) 
# 417209
# (^[-+]?([0-9]+)(\.[0-9]+)?)$'