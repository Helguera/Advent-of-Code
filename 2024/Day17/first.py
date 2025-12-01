

def solve(reg_a, reg_b, reg_c, instr_list, input_list):
    # print("Instr -> {}".format(instr_list))
    # print("Input -> {}".format(input_list))
    # print("------------")

    def get_combo(input):
        if input == 4:
            input = reg_a
        elif input == 5:
            input = reg_b
        elif input == 6:
            input = reg_c
        return input

    output = []
    pointer = 0
    while True:
        instr = int(instr_list[pointer])
        input = int(input_list[pointer])

        # print("Instruction: {} // Input: {}".format(instr, input))
        if instr == 0:
            reg_a = int(reg_a/(2**get_combo(input)))
        elif instr == 1:
            reg_b = reg_b ^ input
        elif instr == 2:
            reg_b = get_combo(input) % 8
        elif instr == 3:
            if reg_a != 0:
                pointer = input
        elif instr == 4:
            reg_b = reg_b ^ reg_c
        elif instr == 5:
            output.append(str(get_combo(input)%8))
        elif instr == 6:
            reg_b = int(reg_a/(2**get_combo(input)))
        elif instr == 7:
            reg_c = int(reg_a/(2**get_combo(input)))
        
        if pointer == len(instr_list) - 1:
            break
        if instr != 3:
            pointer += 1

    return reg_a, reg_b, reg_c, output


if __name__ == "__main__":

    with open("./Day17/input.txt", "r") as file:
        for index, line in enumerate(file):
            if "A" in line:
                reg_a = int(line.split(":")[1].strip())
            elif "B" in line:
                reg_b = int(line.split(":")[1].strip())
            elif "C" in line:
                reg_c = int(line.split(":")[1].strip())
            elif "Program" in line:
                instr_list = [x for i, x in enumerate(line.split(":")[1].strip().replace(",", "")) if i % 2 == 0]
                input_list = [x for i, x in enumerate(line.split(":")[1].strip().replace(",", "")) if i % 2 != 0]
    reg_a, reg_b, reg_c, output = solve(reg_a, reg_b, reg_c, instr_list, input_list)

    print("\nREG A: {} // REG B: {} // REG C: {}".format(reg_a, reg_b, reg_c))
    print("OUTPUT -> {}".format(",".join(output)))


