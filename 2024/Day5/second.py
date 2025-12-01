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
            # print(appearance)
            if appearance in item and number in item and (item.index(appearance) < item.index(number)):
                # print("{} -> NOT VALID!".format(item))

                temp = item[item.index(number)]
                item[item.index(number)] = item[item.index(appearance)]
                item[item.index(appearance)] = temp

                my_func(item)
                return True
    return False

for item in input:
    if my_func(item):
        print("{} -> NOW IS VALID!".format(item))

        result += item[math.floor(len(item)/2)]



print(result)

