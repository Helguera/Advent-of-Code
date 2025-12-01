from sklearn.cluster import DBSCAN
import numpy as np

def find_groups(matrix):
    rows, cols = len(matrix), len(matrix[0])
    data = []

    for r in range(rows):
        for c in range(cols):
            letter = matrix[r][c]
            data.append([r, c, ord(letter)])  

    data = np.array(data)

    clustering = DBSCAN(eps=1, min_samples=1, metric='manhattan').fit(data)

    labels = clustering.labels_
    groups = {}
    for idx, label in enumerate(labels):
        if label not in groups:
            groups[label] = []
        groups[label].append((data[idx][0], data[idx][1]))

    return list(groups.values())

# matrix = [
#     "RRRRIICCFF",
#     "RRRRIICCCF",
#     "VVRRRCCFFF",
#     "VVRCCCJFFF",
#     "VVVVCJJCFE",
#     "VVIVCCJJEE",
#     "VVIIICJJEE",
#     "MIIIIIJJEE",
#     "MIIISIJEEE",
#     "MMMISSJEEE",
# ]

# matrix = [
#     "AAAA",
#     "BBCD",
#     "BBCC",
#     "EEEC"
# ]

matrix = []
with open("/content/input.txt", "r") as archivo:
    for line in archivo:
        matrix.append(line.strip())

matrix = [list(row) for row in matrix]
groups = find_groups(matrix)

# print(groups)


total = 0
for idy, row in enumerate(groups):
    max_x = max([x[0] for x in row])
    min_x = min([x[0] for x in row])
    max_y = max([x[1] for x in row])
    min_y = min([x[1] for x in row])
    nom_x = max_x - min_x
    nom_y = max_y - min_y
    empty_matrix = [["." for _ in range(nom_y + 3)] for _ in range(nom_x + 3)]

    for idx, col in enumerate(row):
        empty_matrix[col[0]+1 - min_x][col[1]+1 - min_y] = str(idy)

    # for row in empty_matrix:
    #     print("".join(row))
    # print()

    group_perimeter = 0 
    for t_idx, t_row in enumerate(empty_matrix):
        for t_idy, t_col in enumerate(t_row):
            if t_col != ".":
                if empty_matrix[t_idx-1][t_idy] == ".":
                    group_perimeter += 1
                if empty_matrix[t_idx+1][t_idy] == ".":
                    group_perimeter += 1
                if empty_matrix[t_idx][t_idy-1] == ".":
                    group_perimeter += 1
                if empty_matrix[t_idx][t_idy+1] == ".":
                    group_perimeter += 1
    total += group_perimeter * len(row)

print(total)
                