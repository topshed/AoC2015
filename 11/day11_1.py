import string
import re
password = "hxbxwxba"
#password = "ghijklmn"
#password = "hxbxxyzz"
alpha = string.ascii_lowercase
trips = []
for s in range(len(alpha)-3):
    chunks = [alpha[i:i+3] for i in range(s, len(alpha), 3)]
    for c in chunks:
        if len(c) ==3:
            trips.append(c)
#print(trips)

def is_valid(p):
    valid = False
    if len(p) == 8:
        if p.islower():
            if 'i' not in p:
                if 'o' not in p:
                    if 'l' not in p:
                        if len(re.findall(r'((\w)\2)', p)) > 1: # non-overlapping?

                            for c in trips:
                                #if re.match(c,p):
                                if c in p:
                                    valid = True
                                    print(c)
                               #else:
                                    #print("no triples")
                        else:
                            print("not enough repeats")
                    else:
                        print("contains l")
                else:
                    print("contains o")
            else:
                print("contains i")
        else:
            print("contains upper")
    else:
        print("too short")

    return(valid)

#print(is_valid("abbcegjk"))

def increment_char(c):
    if ord(c) != 122:
        return(chr(ord(c)+1))
    else:
        return('a')

def increment_password(s):
    new_passwod = ""
    if( (ord(s[len(s)-1]) - 96) == 26 ):
        new_passwod += increment_password(s[:len(s)-1]) + "a"
    else:
        return (s[:len(s)-1] + chr(ord(s[len(s)-1])+1))
    return new_passwod

while not is_valid(password):
    print(password)
    password = increment_password(password)
    
print(password)
password = increment_password(password)

while not is_valid(password):
    print(password)
    password = increment_password(password)
print(password)