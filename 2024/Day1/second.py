list1 = []
list2 = []

result = 0

with open("./Day1/input.txt", "r") as archivo:
    for line in archivo:
        line = line.strip().split("   ")
        list1.append(int(line[0]))
        list2.append(int(line[1]))

dict2 = {}
for item in list2:
    if dict2.get(item, None) is not None:
        dict2[item] += 1
    else:
        dict2[item] = 1

for item in list1:
    result += dict2.get(item, 0) * item

print(result)
