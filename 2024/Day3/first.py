import re

with open("./Day3/input.txt", "r") as file:
    content = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

result = re.findall(pattern, content)

solution = 0
for item in result:
    solution += int(item[0]) * int(item[1])

print(solution)