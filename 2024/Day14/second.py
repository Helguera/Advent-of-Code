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
        print("".join(row))

input = []
matrix_x = 101
matrix_y = 103
seconds = [6600, 6800]

with open("./Day14/input.txt", "r") as file:
    for index, line in enumerate(file):
        match = re.match(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', line.strip())
        if match:
            p1, p2, v1, v2 = map(int, match.groups())
            input.append(Robot(p1, p2, v1, v2))


for second in range(0, seconds[1]):
    matrix = [[" " for _ in range(matrix_x)] for _ in range(matrix_y)]
    for robot in input:
        robot.move(1)
        robot.normalize_matrix(matrix_x, matrix_y)
        matrix[robot.y][robot.x] = "#"
    if second > seconds[0] and second < seconds[1]:
        print("============================")
        print(second+1)
        print_matrix(matrix)



# 6752