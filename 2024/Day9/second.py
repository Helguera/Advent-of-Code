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
        # for i in range(0, int(item)):
        #     mod_content.append(str(count))
        mod_content.append([str(count) * int(item), 0])
        count += 1
    else:
        # for i in range(0, int(item)):
        #     mod_content.append(".")
        mod_content.append(["." * int(item), int(item)])


num_to_move = mod_content.count(".")
print(" ".join([x[0] for x in mod_content]))
# print(mod_content)

def compute(array, next_item):
    result = [x for x in array if x[1]>= len(next_item[0])]
    print(result)

    if result:
        if len(result[0][0]) == len(next_item[0]):
            print("same ")
        else:
            index_to_insert = array.index(result[0][0])
            print(index_to_insert)


result = compute(mod_content, mod_content[len(mod_content) - 1])
