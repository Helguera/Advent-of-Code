import itertools

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
    for row in matrix:
        print("".join(row))

def calculate_antinodes(coord1, coord2):
    distance = (coord1[0]-coord2[0], coord1[1]-coord2[1])
    return [
        (coord1[0]+distance[0], coord1[1]+distance[1]),
        (coord2[0]-distance[0], coord2[1]-distance[1]),
        ]

locations = []
for anthena, coords in data.items():
    combinations = list(itertools.combinations(coords, 2))
    for comb in combinations:
        antinodes = calculate_antinodes(comb[0], comb[1])
        result = [
            x for x in antinodes
            if 0 <= x[0] < max_x
            and 0 <= x[1] < max_y
        ]
        locations += result
        
# print(set(locations))
print(len(set(locations)))




