import re
import math

class Robot():
    def __init__(self, p1, p2, v1, v2):
        self.x = p1
        self.y = p2
        self.vx = v1
        self.vy = v2
        self.quarter = None

    def move(self, seconds):
        self.x = self.x + self.vx*seconds
        self.y = self.y + self.vy*seconds

    def normalize_matrix(self, max_x, max_y):
        self.x = self.x % max_x
        self.y = self.y % max_y

    def __str__(self):
        return "X={} Y={} -- {} {} --> {}".format(self.x, self.y, self.vx, self.vy, self.quarter)

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            if item == []:
                print(".", end="")
            else:
                print(len(item), end="")
        print()

input = []
matrix_x = 101
matrix_y = 103
seconds = 100

with open("./Day14/input.txt", "r") as file:
    for index, line in enumerate(file):
        match = re.match(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', line.strip())
        if match:
            p1, p2, v1, v2 = map(int, match.groups())
            input.append(Robot(p1, p2, v1, v2))

quarter1, quarter2, quarter3, quarter4 = 0, 0, 0, 0
for robot in input:
    robot.move(seconds)
    robot.normalize_matrix(matrix_x, matrix_y)
    if robot.x < math.floor(matrix_x/2) and robot.y < math.floor(matrix_y/2):
        robot.quarter = 1
        quarter1 += 1
    if robot.x > math.floor(matrix_x/2) and robot.y < math.floor(matrix_y/2):
        robot.quarter = 2
        quarter2 += 1
    if robot.x < math.floor(matrix_x/2) and robot.y > math.floor(matrix_y/2):
        robot.quarter = 3
        quarter3 += 1
    if robot.x > math.floor(matrix_x/2) and robot.y > math.floor(matrix_y/2):
        robot.quarter = 4
        quarter4 += 1
    print(robot)

matrix = [[[] for _ in range(matrix_x)] for _ in range(matrix_y)]
for robot in input:
    matrix[robot.y][robot.x].append(robot)
print_matrix(matrix)


print(quarter1*quarter2*quarter3*quarter4)


