import itertools
from tqdm import tqdm

input = []

with open("./Day7/input.txt", "r") as file:
    for index, line in enumerate(file):
        input.append(
            (
                line.split(":")[0].strip(),
                line.split(":")[1].strip().split(" ")
            )
        )

# Delete || operator for part 1 solution
operations = ["*", "+", "||"]

def my_eval(input):

    if "||" in input:
        input = input.replace("||", "")

    return eval(input)

final_result = 0
# print(input)
for comb in tqdm(input):
    numbers = comb[1]
    expected_result = comb[0]

    n = len(numbers) - 1 
    operation_combinations = itertools.product(operations, repeat=n)
    # print([x for x in operation_combinations])
    expressions = []
    for i, ops in enumerate(operation_combinations):
        expression = numbers[0]
        for j, op in enumerate(ops):
            # print("{}{}{}".format(expression, op, numbers[j+1]))
            expression = my_eval("{}{}{}".format(expression, op, numbers[j+1]))
        # print(expected_result, numbers, ops, expression)
        if int(expected_result) == int(expression):
            final_result += int(expression)
            break

print(final_result)
