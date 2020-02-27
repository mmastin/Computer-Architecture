"""CPU functionality."""

import sys

HLT = 0x01 # halt and exit
LDI = 0x82 # set val to int
PRN = 0x47 # print numeric value
MUL = 0xA2
ADD = 0xA0
POP = 0x46
PUSH = 0x45
CALL = 0x50 # call subroutine at address stored
RET = 0x11 # return from a subroutine

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.register[7] = 255
        self.sp = self.register[7]
        self.flag = 0b00000000
        self.branctable = {
            HLT: self.hlt,
            LDI: self.ldi,
            PRN: self.prn,
            POP: self.pop,
            PUSH: self.push,
            CALL: self.call,
            RET: self.ret
        }

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, path):
        """Load a program into memory."""
        try:
            address = 0

            with open(path) as f:
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

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == 'SUB':
            self.reg[reg_a] -= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            IR = self.ram_read(self.pc)
