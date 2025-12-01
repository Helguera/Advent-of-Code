import math
from tqdm import tqdm

with open("./Day11/input.txt", "r") as file:
    input = file.read().strip().split(" ")


blinks = 25

for blink in tqdm(range(blinks)):
    skip_next = False
    for index, stone in enumerate(input):
        if not skip_next:
            # print("NOW STONE {}".format(stone))
            if stone == "0":
                input[index] = str(1)
            elif len(stone) % 2 == 0:
                input[index] = str(stone[0:math.floor(len(stone)/2)]).lstrip("0")
                new_stone = str(stone[math.ceil(len(stone)/2):len(stone)]).lstrip("0")
                input.insert(index+1, "0" if new_stone == "" else new_stone)
                skip_next = True
            else:
                input[index] = str(int(stone) * 2024)
            # print(input)
        else:
            skip_next = False

print(len(input))

