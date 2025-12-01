
my_array = []
with open("./Day4/input.txt", "r") as archivo:
    for line in archivo:
        my_array.append(line.strip())

def find_xmas(y, x, array, direction, found):
    if y < 0 or x < 0 or y > len(array)-1 or x > len(array[0])-1:
        return found
    
    print("{},{} -> letter: {}, direction: {}, total found: {}".format(y,x,array[y][x], direction, found))

    if array[y][x] == "M":
        return found + "M"
    if array[y][x] == "S":
        return found + "S"
    if array[y][x] == "S" or array[y][x] == "M" or direction is None:
        if direction == 1 or direction is None:
            found = find_xmas(y-1, x-1, array, 1, found)
        if direction == 3 or direction is None:
            found = find_xmas(y-1, x+1, array, 3, found)
        if direction == 5 or direction is None:
            found = find_xmas(y+1, x+1, array, 5, found)
        if direction == 7 or direction is None:
            found = find_xmas(y+1, x-1, array, 7, found)

    return found


# my_array = [
#     "S-S----",
#     "-A--S-M",
#     "M-M--A-",
#     "----M-S",
#     "M-S----",
#     "-A--M-M",
#     "M-S--A-",
#     "----S-S",
#     "M-S----",
#     "-A-----",
#     "S-M----"
# ]

total = 0
for index_y, y in enumerate(my_array):
    for index_x, x in enumerate(y):
        if my_array[index_y][index_x] == "A":
            print('--------------------')
            sol = find_xmas(index_y, index_x, my_array, None, "")
            print(sol if sol != "" else "Nothing :(")
            if sol in [
                "SSMM", "MSSM", "MMSS", "SMMS"
            ]:
                print("MATCH!!")
                total += 1

print(total)
