
list1 = []
list2 = []
result = 0

with open("./Day1/input.txt", "r") as archivo:
    for line in archivo:
        line = line.strip().split("   ")
        list1.append(int(line[0]))
        list2.append(int(line[1]))

list1.sort(reverse=True)
list2.sort(reverse=True)

for i in range(0, len(list1)):
    result += abs(list1.pop()-list2.pop())
print(result)


