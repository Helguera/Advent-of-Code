import re

with open("./Day3/input.txt", "r") as file:
    content = file.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

result = re.findall(pattern, content)

solution = 0
dont = False
for item in result:
    if item == 'don\'t()':
        dont = True
    elif item == 'do()':
        dont = False
    elif dont == False:
        out = re.match(r"mul\((\d+),(\d+)\)", item)
        num1, num2 = map(int, out.groups())
        solution += int(num1) * int(num2)

print(solution)