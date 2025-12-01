with open("./Day9/input.txt", "r") as file:
    content = file.read()

content = "2333133121414131402"

# content = "19191919191"

# content = "919191919919191919199191919191991"

# content = "111111"

# content = "1111111111111911111111111"

# 00...111...2...333.44.5555.6666.777.888899
# 0099811188827773336446555566


#  89558806610
#  89558806610
#  1343135600213
#  134313560021
#  81705036806


mod_content = []
count = 0
for index, item in enumerate(content):
    if index % 2 == 0:
        for i in range(0, int(item)):
            mod_content.append(str(count))
        count += 1
    else:
        for i in range(0, int(item)):
            mod_content.append(".")


num_to_move = mod_content.count(".")
print(" ".join(mod_content))
print()

count = 0
for i in range(len(mod_content)-1, 0, -1):
    # print(mod_content.index("."), i, " ----- ", " ".join(mod_content))
    if mod_content[i].isdigit() and mod_content.index(".") < i:
        mod_content[mod_content.index(".")] = mod_content[i]
        count += 1

for i in range(len(mod_content)-1, 0, -1):
    if count == 0:
        break
    if mod_content[i].isdigit():
        del mod_content[i]
        count -= 1

total = 0
for index, i in enumerate(mod_content):
    if mod_content[index].isdigit():
        total += (index * int(i))


print(" ".join(mod_content))
print(total)