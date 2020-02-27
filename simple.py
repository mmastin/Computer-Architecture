import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 # save a value to a register
PRINT_REGISTER = 5 # will print the value in a register
ADD = 6 # add 2 registers, store the result in 1st register
PUSH = 7
POP = 8

# memory = [
#     PRINT_BEEJ, 
#     SAVE, 
#     65,
#     2,
#     SAVE,
#     30,
#     3,
#     ADD,
#     2,
#     3,
#     PRINT_REGISTER,
#     2,
#     HALT
# ]

memory = [0] * 32

register = [0] * 8

pc = 0  # program counter 

SP = 7 # stack pointer is r7

def load_memory(filename):
    try:
        address = 0

        with open(filename) as f:
            for line in f:
                comment_split = line.strip().split('#')

                value = comment_split[0].strip()

                if value == '':
                    continue

                num = int(value)
                memory[address] = num
                address += 1

    except FileNotFoundError:
        print('file not found')
        sys.exit(2)

if len(sys.argv) != 2:
    print('error: must have a file name')
    sys.exit(1)

load_memory(sys.argv[1])

while True:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print('Beej!')
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
    elif command == PUSH:
        reg = memory[pc + 1]
        val = register[reg]
        register[SP] -= 1
        memory[register[SP]] = val
        pc += 2
    elif command == POP:
        reg = memory[pc + 1]
        val = memory[register[SP]]
        register[reg] = val
        register[SP] += 1
        pc += 2
    elif command == HALT:
        sys.exit(0)

    else:
        print('I did not understand command')
        sys.exit(1)