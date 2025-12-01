

def in_order(list):
    dup = list.copy()
    for reverse in [False, True]:
        list.sort(reverse=reverse)
        if dup == list:
            return True
    return False

def adjacent(list):
    precedent = list[0]
    for item in list[1:]:
        if precedent == item:
            return False
        if abs(precedent - item) > 3:
            return False
        precedent = item
    return True

safe = 0

checks = [
    in_order, adjacent
]
with open("./Day2/input.txt", "r") as file:
    for line in file:
        input_list = [int(x) for x in line.strip().split(" ")]
        for index in range(-1, len(input_list)):
            dup = input_list.copy()
            if index >= 0:
                del dup[index]
            if in_order(dup) and adjacent(dup):
                safe+=1
                break


print(safe)