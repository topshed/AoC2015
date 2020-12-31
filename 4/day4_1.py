import hashlib
input = "ckczppom"

number=0
result = '123456'
while str(result)[:6] != '000000':
    text = input+str(number)
    result = hashlib.md5(text.encode()).hexdigest()
    number+=1

print(result,number)