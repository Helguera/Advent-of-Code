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

dir = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
coords = set()

while True:
    coords.add((or_x, or_y))

    next_y = or_y + directions[dir][0]
    next_x = or_x + directions[dir][1]

    if not (0 <= next_y < max_y and 0 <= next_x < max_x):
        break

    if my_array[next_y][next_x] == '#':
        dir = (dir+1) % 4
    else:
        or_x = next_x
        or_y = next_y

print(coords)
print(len(coords))