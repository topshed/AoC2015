import numpy as np
puzzle_input= 33100000
max_number = puzzle_input // 11
houses = np.zeros(max_number + 1)
for i in range(1, max_number + 1):
    houses[i:i * 50:i] += 11 * i
print(np.where(houses >= puzzle_input)[0][0])