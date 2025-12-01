import copy
import tqdm

my_array = []
with open("./Day6/input.txt", "r") as file:
    for index, line in enumerate(file):
        if '^' in line:
            or_y = index
            or_x = line.index('^')
        my_array.append([x for x in line.strip()])


print("INIT COORDS: X={} Y={}".format(or_x, or_y))

max_x = len(my_array[0])
max_y = len(my_array)
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] 


def print_array(my_array):
    for y in my_array:
        for x in y:
            print(x,  end='')
        print()

def find_loop(array, or_x, or_y):
    dir = 0
    coords = []

    while True:
        if [or_x, or_y, dir] in coords:
            return True
        else:
            coords.append([or_x, or_y, dir])

        next_y = or_y + directions[dir][0]
        next_x = or_x + directions[dir][1]

        if not (0 <= next_y < max_y and 0 <= next_x < max_x):
            return False

        if array[next_y][next_x] == '#':
            dir = (dir+1) % 4
        else:
            or_x = next_x
            or_y = next_y

dir = 0
coords = set()

y = or_y
x = or_x
while True:
    coords.add((x, y))

    next_y = y + directions[dir][0]
    next_x = x + directions[dir][1]

    if not (0 <= next_y < max_y and 0 <= next_x < max_x):
        break

    if my_array[next_y][next_x] == '#':
        dir = (dir+1) % 4
    else:
        x = next_x
        y = next_y

coords.remove((or_x, or_y))
total = 0
for coord in tqdm.tqdm(coords):
    dup = copy.deepcopy(my_array)
    # print_array(dup)

    dup[coord[1]][coord[0]] = '#'
    # print("---------------")
    if find_loop(dup, or_x, or_y):
        total +=1
print(len(coords))
print(total)



