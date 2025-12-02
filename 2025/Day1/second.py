
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
        new_starting_point = (starting_point - num_clicks) % 100
    else:
        new_starting_point = (starting_point + num_clicks) % 100

    if starting_point == 0:
        result += 1
    if num_clicks > 100:
        result += int(num_clicks/100)
    
    print("DIAL IS ROTATED {} FROM {} TO POINT AT {}".format(input.strip(), starting_point, new_starting_point))

    if direction == "L" and starting_point < new_starting_point and new_starting_point != 0 and starting_point != 0:
        print("     L extra")
        result += 1
    elif direction == "R" and starting_point > new_starting_point and new_starting_point != 0 and starting_point != 0:
        print("     R extra")
        result += 1

    starting_point = new_starting_point

    
print(result)
