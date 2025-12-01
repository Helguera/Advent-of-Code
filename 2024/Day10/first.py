from copy import deepcopy

matrix = []
starting_points = []
total_ends = 0

with open("./Day10/input.txt", "r") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == ".":
                char = -1
            elif int(char) == 0:
                starting_points.append((x, y))
            elif int(char) == 9:
                total_ends += 1
        matrix.append([int(x) if x.isdigit() else -1 for x in line.strip()])

max_x = len(matrix[0])
max_y = len(matrix)

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(x) for x in row]))

def run_matrix(x, y, matrix, ends):
    if matrix[y][x] == 9:
        new_matrix = deepcopy(matrix)
        # ACTIVATE THIS LINE FOR PART 1
        # new_matrix[y][x] = 0
        return ends + 1, new_matrix
    if x+1 < max_x and matrix[y][x+1] == matrix[y][x]+1:
        ends, matrix = run_matrix(x+1, y, matrix, ends)
    if y+1 < max_y and matrix[y+1][x] == matrix[y][x]+1:
        ends, matrix = run_matrix(x, y+1, matrix, ends)
    if x-1 >= 0 and matrix[y][x-1] == matrix[y][x]+1:
        ends, matrix = run_matrix(x-1, y, matrix, ends)
    if y-1 >= 0 and matrix[y-1][x] == matrix[y][x]+1:
        ends, matrix = run_matrix(x, y-1, matrix, ends)
    return ends, matrix

final_result = 0
for sp in starting_points:
    result, _ = run_matrix(sp[0], sp[1], matrix, 0)
    # print(result)
    final_result += result

print("FINAL RESULT -> {}".format(final_result))