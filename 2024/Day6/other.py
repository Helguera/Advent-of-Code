import sys


sys.setrecursionlimit(20000)  



my_array = []
with open("./Day6/input2.txt", "r") as file:
    for index, line in enumerate(file):
        if '^' in line:
            or_y = index
            or_x = line.index('^')
            line = line.replace('^', '1')
        my_array.append([x for x in line.strip()])


print("INIT COORDS: X={} Y={}".format(or_x, or_y))


def next_move_valid(x, y, array, direction):
    if direction == 1:
        if y-1 < 0: return -1
        elif array[y-1][x] == '#':
            return 0
    elif direction == 2:
        if x+1 > len(array[0])-1: return -1
        elif array[y][x+1] == '#':
            return 0
    elif direction == 3:
        if y+1 > len(array)-1: return -1
        elif array[y+1][x] == '#':
            return 0
    elif direction == 4:
        if x-1 < 0: return -1
        elif array[y][x-1] == '#':
            return 0
    return 1

def print_array(my_array):
    for y in my_array:
        for x in y:
            print(x,  end='')
        print()

def find_path(x, y, my_array, steps):
    print("----------------")
    print_array(my_array)
    print(x, y)
    if my_array[y][x] == '1':
        nmv = next_move_valid(x, y, my_array, 1)
        if nmv == 1:
            my_array[y][x] = '.'
            my_array[y-1][x] = '1'
            steps.add((y,x))
            steps = find_path(x, y-1, my_array, steps)
        elif nmv == 0:
            my_array[y][x] = '2'
            steps = find_path(x, y, my_array, steps)
        elif nmv == -1:
            return steps
    if my_array[y][x] == '2':
        nmv = next_move_valid(x, y, my_array, 2)
        if nmv == 1:
            my_array[y][x] = '.'
            my_array[y][x+1] = '2'
            steps.add((y,x))
            steps = find_path(x+1, y, my_array, steps)
        if nmv == 0:
            my_array[y][x] = '3'
            steps = find_path(x, y, my_array, steps)
        elif nmv == -1:
            return steps
    if my_array[y][x] == '3':
        nmv = next_move_valid(x, y, my_array, 3)
        if nmv == 1:
            my_array[y][x] = '.'
            my_array[y+1][x] = '3'
            steps.add((y,x))
            steps = find_path(x, y+1, my_array, steps)
        if nmv == 0:
            my_array[y][x] = '4'
            steps = find_path(x, y, my_array, steps)
        elif nmv == -1:
            return steps
    if my_array[y][x] == '4':
        nmv = next_move_valid(x, y, my_array, 4)
        if nmv == 1:
            my_array[y][x] = '.'
            my_array[y][x-1] = '4'
            steps.add((y,x))
            steps = find_path(x-1, y, my_array, steps)
        if nmv == 0:
            my_array[y][x] = '1'
            steps = find_path(x,y, my_array, steps)
        elif nmv == -1:
            return steps
    return steps

steps = find_path(or_x, or_y, my_array, set())
print('')
print(len(steps)+1)


