
my_array = []
with open("./Day4/input.txt", "r") as archivo:
    for line in archivo:
        my_array.append(line.strip())


find_string = "XMAS"

def find_xmas(y, x, array, letter, direction, found):
    print("{},{} -> letter: {}, direction: {}, total found: {}".format(y,x,letter, direction, found))

    if y < 0 or x < 0 or y > len(array)-1 or x > len(array[0])-1:
        return found
    if array[y][x] == letter:
        if letter == "S":
            print("FOUND!!")
            return found + 1
        if direction == 1 or direction is None:
            found = find_xmas(y-1, x-1, array, find_string[find_string.find(letter) + 1], 1, found)
        if direction == 2 or direction is None:
            found = find_xmas(y-1, x, array, find_string[find_string.find(letter) + 1], 2, found)
        if direction == 3 or direction is None:
            found = find_xmas(y-1, x+1, array, find_string[find_string.find(letter) + 1], 3, found)
        if direction == 4 or direction is None:
            found = find_xmas(y, x+1, array, find_string[find_string.find(letter) + 1], 4, found)
        if direction == 5 or direction is None:
            found = find_xmas(y+1, x+1, array, find_string[find_string.find(letter) + 1], 5, found)
        if direction == 6 or direction is None:
            found = find_xmas(y+1, x, array, find_string[find_string.find(letter) + 1], 6, found)
        if direction == 7 or direction is None:
            found = find_xmas(y+1, x-1, array, find_string[find_string.find(letter) + 1], 7, found)
        if direction == 8 or direction is None:
            found = find_xmas(y, x-1, array, find_string[find_string.find(letter) + 1], 8, found)

    return found




total = 0
for index_y, y in enumerate(my_array):
    for index_x, x in enumerate(y):
        sol = find_xmas(index_y, index_x, my_array, "X", None, 0)
        total += sol

print(total)
