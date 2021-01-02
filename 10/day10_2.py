def lookandsay(number):
    result = ""
 
    repeat = number[0]
    number = number[1:]+" "
    times = 1
 
    for actual in number:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1
 
    return result
 
num = "1113122113"
 
for i in range(51):
    print(i,len(num))
    num = lookandsay(num)