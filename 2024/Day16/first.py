import time
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

matrix = []
start_x, start_y = None, None
with open("./Day16/input.txt", "r") as file:
    for index, line in enumerate(file):
        if 'S' in line:
            start_x, start_y = line.index('S'), index
        matrix.append(line.strip())

def print_matrix(matrix):
    for col in matrix:
        print(col)

print_matrix(matrix)
print(start_x, start_y)

def print_tree(node, level=0):
    # print("  " * level + f"- {node.value}")
    for child, weight in node.children:
        print("  " * (level + 1) + f"(Weight: {weight})")
        print_tree(child, level + 1)

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.children = []
        self.x = x
        self.y = y

    def add_child(self, value, weight):
        self.children.append((value, weight))

starting_node = Node('S', start_x, start_y)
limit_x = len(matrix[0])
limit_y = len(matrix)

# direction -> 1:>, 2:v, 3:<, 4:^
def next_pos(matrix, x, y, direction, parent_node, visited):
    local_visited = deepcopy(visited)
    temp = deepcopy(matrix)
    temp[y] = temp[y][:x] + "$" + temp[y][x+1:]
    # print_matrix(temp)
    # time.sleep(.5)
    # print("X: {} Y:{} Direction: {}".format(x, y, direction))
    # print(local_visited)
    # print_tree(starting_node)
    if direction != 3 and x+1 < limit_x and matrix[y][x+1] != '#' and (x+1, y) not in local_visited:
        weigth = 1 if direction == 1 else 1001
        child = Node(matrix[y][x+1], x+1, y)
        parent_node.add_child(child, weigth)
        if matrix[y][x+1] == "?":
            return
        local_visited.append((x+1, y))
        next_pos(matrix, x+1, y, 1, child, local_visited)
        local_visited.pop()
    if direction != 4 and y+1 < limit_y and matrix[y+1][x] != '#' and (x, y+1) not in local_visited:
        weigth = 1 if direction == 2 else 1001
        child = Node(matrix[y+1][x], x, y+1)
        parent_node.add_child(child, weigth)
        if matrix[y+1][x] == "?":
            return
        local_visited.append((x, y+1))
        next_pos(matrix, x, y+1, 2, child, local_visited)
        local_visited.pop()
    if direction != 1 and x-1 > 0 and matrix[y][x-1] != '#' and (x-1, y) not in local_visited:
        weigth = 1 if direction == 3 else 1001
        child = Node(matrix[y][x-1], x-1, y) 
        parent_node.add_child(child, weigth)
        if matrix[y][x-1] == "?":
            return
        local_visited.append((x-1, y))
        next_pos(matrix, x-1, y, 3, child, local_visited)
        local_visited.pop()
    if direction != 2 and y-1 > 0 and matrix[y-1][x] != '#' and (x, y-1) not in local_visited:
        weigth = 1 if direction == 4 else 1001
        child = Node(matrix[y-1][x], x, y-1)
        parent_node.add_child(child, weigth)
        if matrix[y-1][x] == "?":
            return
        local_visited.append((x, y-1))
        next_pos(matrix, x, y-1, 4, child, local_visited)
        local_visited.pop()
    return

print("FINDING ALL POSSIBILITIES")
result = next_pos(matrix, start_x, start_y, 1, starting_node, [(start_x, start_y)])

# print_tree(starting_node)

def find_minimum_path_with_positions(node, target, current_weight=0, current_path=None):
    if current_path is None:
        current_path = []

    current_path.append((node.value, current_weight, node.x, node.y))

    if node.value == target:
        return (current_path, current_weight)

    min_path = None
    min_weight = float('inf')
    for child, weight in node.children:
        result = find_minimum_path_with_positions(child, target, current_weight + weight, current_path.copy())
        if result:
            path, total_weight = result
            if total_weight < min_weight:
                min_path = path
                min_weight = total_weight

    return (min_path, min_weight) if min_path else None

print("FINDING NOW BEST PATH")
result = find_minimum_path_with_positions(starting_node, "?")
if result:
    path, total_weight = result
    print("Path followed:")
    for value, weight, x, y in path:
        print(f"Node: {value}, Position: ({x}, {y}), Weight to here: {weight}")
    print(f"Total Weight: {total_weight}")
else:
    print("Target node not found.")


