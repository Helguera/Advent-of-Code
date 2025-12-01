
from first import solve
import multiprocessing


# reg_a = 0
# while True:
#     if (reg_a % 1000000) == 0:
#         print("REG_A -> {}".format(reg_a))
#     *_, output = solve(reg_a, reg_b, reg_c, instr_list, input_list)
#     if ",".join(output) == program:
#         print("FOUND -> REG_A= {}".format(reg_a))
#         break
#     reg_a += 1

def worker(start, step, reg_b, reg_c, instr_list, input_list, program, queue):
    reg_a = start
    while True:
        if (reg_a % 1000000) == 0:
            print(f"Process {start}: REG_A -> {reg_a}")
        *_, output = solve(reg_a, reg_b, reg_c, instr_list, input_list)
        if ",".join(output) == program:
            queue.put(reg_a) 
            break
        reg_a += step

def main():
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
                program = line.split(":")[1].strip()

    
    num_processes = multiprocessing.cpu_count()  
    queue = multiprocessing.Queue() 

    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(
            target=worker,
            args=(i, num_processes, reg_b, reg_c, instr_list, input_list, program, queue)
        )
        processes.append(process)
        process.start()

    found = queue.get()  

    for process in processes:
        process.terminate()
        process.join()

    print(f"FOUND -> REG_A = {found}")

if __name__ == "__main__":
    main()


