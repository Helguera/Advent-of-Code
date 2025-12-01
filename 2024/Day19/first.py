import copy
import time


# So Im not sure how I made this work, but it works. My logic is:
# Start from the back of the design, delete one by one a letter and check if the rest matches a pattern
# If it matches, delete the part found and repeat with the rest
# I do it two times, starting from the right, and from the left
# The latest scenario is this one -> abcd, dxa, abc, bcd as patterns, abcdxabcd as design. In this case, my logic will not work
# So, I delete one pattern and do the whole process again, repeat with all patterns

designs = []
with open("./Day19/input.txt", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            patterns = line.strip().replace(" ", "").split(",")
            patterns = sorted(patterns, key=len, reverse=True)
        elif line.strip() != "":
            designs.append(line.strip())

# print(patterns)

possible = []

for design in designs:
    # print()
    des_copy = design
    solution = ""
    while len(des_copy) > 0:
        # time.sleep(0.01)
        # print("CHECK {}, SOLUTION {}".format(des_copy, solution))
        if des_copy in patterns:
            solution += des_copy
            des_copy = design[len(solution):len(design)]
        else:
            des_copy = des_copy[:-1]
        if solution == design:
            possible.append(solution)
            break

designs = [x for x in designs if x not in possible]
for design in designs:
    # print()
    des_copy = design
    solution = ""
    patterns_copy = copy.copy(patterns)
    count = 0
    while len(des_copy) > 0:
        # time.sleep(0.01)
        # print("CHECK REVERSE {}, PATTERNS {}, COUNT {}, SOLUTION {}".format(des_copy, patterns_copy, count, solution))
        if des_copy in patterns_copy:
            solution = des_copy + solution
            des_copy = design[0:len(design)-len(solution)]
        else:
            des_copy = des_copy[1:]
            if len(des_copy) == 0 and count < len(patterns)-1:
                des_copy = design
                patterns_copy = copy.copy(patterns)
                # print(len(patterns_copy), count-1)
                del patterns_copy[count]
                count += 1
                solution = ""
        if solution == design:
            possible.append(solution)
            break

# print(possible)
# print([x for x in designs if x not in possible])



print(len(possible))




