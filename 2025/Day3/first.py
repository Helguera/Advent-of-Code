
input_list = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

with open("2025/Day3/input.txt", "r") as f:
    input_list = [line.strip() for line in f]

result = sum(
    [
        int(max(item[:-1]) + max(item[item.index(max(item[:-1]))+1:]))
        for item in input_list
    ]
)


print(result)