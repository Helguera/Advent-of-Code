
input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""



input = input.split("\n")

with open("2025/Day4/input.txt", "r") as f:
    input = [line.strip() for line in f]


coords = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,+1), (-1, 0)]
max_x = len(input[0])
max_y = len(input)
result = 0
for y, row in enumerate(input):
    for x, item in enumerate(row):
        if input[y][x] == "@":
            count = 0
            for coord_x, coord_y in coords:
                if x+coord_x >= 0 and x+coord_x < max_x and y+coord_y >= 0 and y+coord_y < max_y and input[y+coord_y][x+coord_x] == '@':
                    count+=1

            if count < 4:
                result += 1


print(result)
            
