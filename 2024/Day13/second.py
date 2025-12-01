

import numpy as np
import re

input = []
pattern = r"([XY])\s*([+\-=])\s*(\d+)"
with open("./Day13/input.txt", "r") as file:
    lines = file.readlines()

    temp_str = ""
    for index, line in enumerate(lines):
        temp_str += line
        if ((index + 1) % 4 == 0 and index != 0) or len(lines) -1 == index:
            matches = re.findall(pattern, temp_str)
            temp_str = ""
            input.append([
                    (int(matches[0][2]), int(matches[1][2])),
                    (int(matches[2][2]), int(matches[3][2])),
                    (int(matches[4][2]) + 10000000000000, int(matches[5][2]) + 10000000000000)
            ])

def calculate_equation(input):
    coefficients = np.array([
        [input[0][0], input[1][0]],
        [input[0][1], input[1][1]]
    ])
    constants = np.array([input[2][0], input[2][1]])
    solution = np.linalg.solve(coefficients, constants)
    return solution

def solve(input):
    a1, b1 = input[0][0], input[1][0]
    a2, b2 = input[0][1], input[1][1]
    c1, c2 = input[2][0], input[2][1]

    det = a1 * b2 - a2 * b1
    if det == 0:
        return # No solution 

    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1

    x = det_x / det
    y = det_y / det

    return x, y

print()
coins = 0
for item in input:
    A, B = solve(item)
    # print(A, B)
    if A.is_integer() and B.is_integer():
        coins += (int(A)*3 + int(B))


print(coins)

