
input_list = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

with open("2025/Day1/input.txt", "r") as f:
    input_list = f.readlines()

result = 0
starting_point = 50
for input in input_list:
    direction = input[:1]
    num_clicks = int(input[1:])
    if direction == "L":
        starting_point = (starting_point - num_clicks) % 100
    else:
        starting_point = (starting_point + num_clicks) % 100

    if starting_point == 0:
        result += 1
    
    # print("DIAL IS ROTATED {} TO POINT AT {}".format(input, starting_point))
print(result)
