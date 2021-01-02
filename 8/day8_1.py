code_chars = 0
string_chars = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        no_quotes = line[1:-1]
        print(line, no_quotes)
        decoded = bytes(no_quotes, "utf-8").decode("unicode_escape")
        code_chars+=len(line)
        string_chars+=len(decoded)
        print(len(line),len(decoded))
print(code_chars-string_chars)