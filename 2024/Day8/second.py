import itertools
import math
import sys

matrix = []
data = {}
max_x = 0
max_y = 0
with open("./Day8/input.txt", "r") as file:
    for y, line in enumerate(file):
        max_x = len(line.strip())
        for x, char in enumerate(line.strip()):
            if char != ".":
                if char in data:
                    data[char].append((x,y))
                else:
                    data[char] = [(x,y)]
        matrix.append([char for char in line.strip()])
        max_y += 1

def print_matrix(matrix):
    print("  ", end="")
    for i in range(len(matrix[0])):
        print(i,end="")
    print()
    for index, row in enumerate(matrix):
        print(index, "".join(row))

def calculate_antinodes(coord1, coord2, max_x, max_y):
    distance = (coord1[0]-coord2[0], coord1[1]-coord2[1])
    antinodes = []
    antinodes.append((coord1[0], coord1[1]))
    antinodes.append((coord2[0], coord2[1]))

    count = 0
    while True:
        count += 1
        if 0 <= coord1[0]+distance[0]*count < max_x and 0 <= coord1[1]+distance[1]*count < max_y:
            antinodes.append((coord1[0]+distance[0]*count, coord1[1]+distance[1]*count))
        else:
            break
        
    count = 0
    while True:
        count += 1
        if 0 <= coord2[0]-distance[0]*count < max_x and 0 <= coord2[1]-distance[1]*count < max_y:
            antinodes.append((coord2[0]-distance[0]*count, coord2[1]-distance[1]*count))
        else:
            break
    return antinodes

locations = []
for anthena, coords in data.items():
    combinations = list(itertools.combinations(coords, 2))
    for comb in combinations:
        antinodes = calculate_antinodes(comb[0], comb[1], max_x, max_y)
        locations += antinodes
        
# print(combinations)
print(len(set(locations)))


# for item in locations:
#     matrix[item[1]][item[0]] = "#"

# print_matrix(matrix)



