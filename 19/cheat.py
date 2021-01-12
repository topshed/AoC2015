replacements = []

medicine = None

for line in open("input.txt"):
    parts = line.strip().split(" => ")
    if len(parts) == 1:
        if not line.strip():
            continue
        medicine = line.strip()
        continue
    replacements.append((parts[0], parts[1]))


def part1():
    molecules = set()
    for src, repl in replacements:
        idx = 0
        while src in medicine:
            idx = medicine.find(src, idx+1)
            if idx == -1:
                break
            molecules.add(medicine[:idx] + repl + medicine[idx + len(src):])
    return len(molecules)


def part2():
    med = medicine
    count = 0
    while med != 'e':
        for src, repl in replacements:
            if repl in med:
                med = med.replace(repl, src, 1)
                count += 1
    return count

print(part2())