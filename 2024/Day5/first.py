import math
conditions = []
input = []
result = 0

with open("./Day5/input.txt", "r") as archivo:
    for line in archivo:
        if '|' in line:
            condition = [int(line.strip().split("|")[0]), int(line.strip().split("|")[1])]
            conditions.append(condition)
        elif line != '':
            try:
                input.append([int(x) for x in line.strip().split(',')])
            except:
                pass


def my_func(item):
    for number in item:
        for appearance in [x[1] for x in conditions if x[0] == number]:
            if appearance in item and number in item and (item.index(appearance) < item.index(number)):
                # print("{} -> NOT VALID!".format(item))
                return False
    return True

for item in input:
    if my_func(item):          
        print("{} -> VALID!!".format(item))
        result += item[math.floor(len(item)/2)]


print(result)

